import 'package:flutter/material.dart';
import '../../../app/mock_data.dart';
import '../../../widgets/primary_button.dart';

class StartNewBatchPage extends StatefulWidget {
  const StartNewBatchPage({super.key});

  @override
  State<StartNewBatchPage> createState() => _StartNewBatchPageState();
}

class _StartNewBatchPageState extends State<StartNewBatchPage> {
  // State Variables
  int _selectedCropIndex = 0;
  bool _isAutoMode = true;
  double _targetTemp = 60.0;
  
  // Controllers
  final TextEditingController _weightController = TextEditingController();
  final TextEditingController _traysController = TextEditingController();
  final TextEditingController _durationController = TextEditingController();

  @override
  void initState() {
    super.initState();
    // Initialize with the first crop's auto settings
    _syncAutoSettings();
  }

  @override
  void dispose() {
    _weightController.dispose();
    _traysController.dispose();
    _durationController.dispose();
    super.dispose();
  }

  // logic to sync UI with MockData when in Auto Mode
  void _syncAutoSettings() {
    if (_isAutoMode) {
      final selectedCrop = MockData.crops[_selectedCropIndex];
      setState(() {
        _targetTemp = selectedCrop.tempC;
        _durationController.text = selectedCrop.durationHours.toString();
      });
    }
  }

  void _handleStartBatch() {
    final selectedCrop = MockData.crops[_selectedCropIndex];
    
    // Data payload for your Flask backend
    final batchData = {
      "device_id": MockData.defaultDeviceId,
      "crop_name": selectedCrop.name,
      "mode": _isAutoMode ? "AUTO" : "MANUAL",
      "target_temp": _targetTemp,
      "duration_hours": int.tryParse(_durationController.text) ?? selectedCrop.durationHours,
      "weight_kg": double.tryParse(_weightController.text) ?? 0.0,
      "trays": int.tryParse(_traysController.text) ?? 1,
    };

    print("Sending to Flask: $batchData");
    
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Starting ${selectedCrop.name} batch...')),
    );
    
    // Add your http.post logic here
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    
    // PREVIOUS COLORS RESTORED
    final accentColor = isDark ? const Color(0xFF00D4AA) : const Color(0xFF1976D2);
    final bgColor = isDark ? const Color(0xFF0A192F) : const Color(0xFFF5F7FA);

    return Scaffold(
      backgroundColor: bgColor, // Restored background
      appBar: AppBar(
        title: const Text('Start New Batch'),
        backgroundColor: Colors.transparent, // Restored transparency
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 1. SELECT CROP
            Text('Select Crop *', style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 12),
            Wrap(
              spacing: 12,
              runSpacing: 12,
              children: List.generate(MockData.crops.length, (i) {
                final crop = MockData.crops[i];
                final isSelected = _selectedCropIndex == i;
                return GestureDetector(
                  onTap: () {
                    setState(() => _selectedCropIndex = i);
                    _syncAutoSettings();
                  },
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                    decoration: BoxDecoration(
                      // Restored teal/blue opacity for selected cards
                      color: isSelected ? accentColor.withOpacity(0.15) : (isDark ? const Color(0xFF112240) : Colors.white),
                      borderRadius: BorderRadius.circular(15),
                      border: Border.all(
                        color: isSelected ? accentColor : (isDark ? const Color(0xFF1E3A5F) : Colors.grey[300]!),
                        width: 2,
                      ),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(crop.emoji, style: const TextStyle(fontSize: 20)),
                        const SizedBox(width: 8),
                        Text(
                          crop.name,
                          style: TextStyle(
                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                            // Restored text color
                            color: isSelected ? accentColor : (isDark ? Colors.white70 : Colors.black87),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),
            ),

            const SizedBox(height: 30),

            // 2. MODE SELECTION
            Text('Drying Mode', style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.all(4),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF112240) : Colors.grey[200],
                borderRadius: BorderRadius.circular(12),
              ),
              child: Row(
                children: [
                  _buildModeTab('Auto', _isAutoMode, isDark, accentColor, () {
                    setState(() => _isAutoMode = true);
                    _syncAutoSettings();
                  }),
                  _buildModeTab('Manual', !_isAutoMode, isDark, accentColor, () {
                    setState(() => _isAutoMode = false);
                  }),
                ],
              ),
            ),

            const SizedBox(height: 30),

            // 3. INPUT FIELDS
            Row(
              children: [
                Expanded(child: _buildField('Weight (kg)', '0.0', _weightController, isDark, keyboard: TextInputType.number)),
                const SizedBox(width: 15),
                Expanded(child: _buildField('Trays Used', '1', _traysController, isDark, keyboard: TextInputType.number)),
              ],
            ),

            const SizedBox(height: 25),

            // 4. TEMPERATURE SLIDER
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text('Target Temp: ${_targetTemp.toInt()}°C', style: const TextStyle(fontWeight: FontWeight.bold)),
                if (_isAutoMode) Text('Auto-Optimized', style: TextStyle(color: accentColor, fontSize: 12)),
              ],
            ),
            Slider(
              value: _targetTemp,
              min: 30,
              max: 80,
              activeColor: accentColor,
              inactiveColor: accentColor.withOpacity(0.2), // Restored subtle track
              onChanged: _isAutoMode ? null : (v) => setState(() => _targetTemp = v),
            ),

            const SizedBox(height: 15),

            // 5. DURATION FIELD (Locked in Auto Mode)
            _buildField(
              'Drying Duration (Hours)', 
              'Time in hours', 
              _durationController, 
              isDark, 
              enabled: !_isAutoMode, // Locked in Auto
              keyboard: TextInputType.number,
            ),

            const SizedBox(height: 40),

            // START BUTTON
            SizedBox(
              width: double.infinity,
              height: 55,
              child: ElevatedButton(
                onPressed: _handleStartBatch,
                style: ElevatedButton.styleFrom(
                  backgroundColor: accentColor,
                  foregroundColor: isDark ? const Color(0xFF0A192F) : Colors.white,
                  elevation: 0,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                ),
                child: const Text('START DRYING BATCH', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, letterSpacing: 1.1)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Helper Widget for Mode Tabs
  Widget _buildModeTab(String label, bool isActive, bool isDark, Color accentColor, VoidCallback onTap) {
    return Expanded(
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 12),
          decoration: BoxDecoration(
            color: isActive ? (isDark ? const Color(0xFF1E3A5F) : Colors.white) : Colors.transparent,
            borderRadius: BorderRadius.circular(10),
            boxShadow: isActive ? [const BoxShadow(color: Colors.black12, blurRadius: 4)] : [],
          ),
          child: Text(
            label,
            textAlign: TextAlign.center,
            style: TextStyle(
              fontWeight: isActive ? FontWeight.bold : FontWeight.normal,
              color: isActive ? accentColor : Colors.grey,
            ),
          ),
        ),
      ),
    );
  }

  // Helper Widget for Input Fields
  Widget _buildField(String label, String hint, TextEditingController controller, bool isDark, {bool enabled = true, TextInputType keyboard = TextInputType.text}) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w500, color: Colors.grey)),
        const SizedBox(height: 8),
        TextField(
          controller: controller,
          enabled: enabled,
          keyboardType: keyboard,
          style: TextStyle(color: enabled ? (isDark ? Colors.white : Colors.black) : Colors.grey),
          decoration: InputDecoration(
            hintText: hint,
            filled: true,
            fillColor: isDark ? const Color(0xFF112240) : Colors.grey[100],
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(12), 
              borderSide: BorderSide(color: isDark ? const Color(0xFF1E3A5F) : Colors.transparent),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(12),
              borderSide: BorderSide(color: isDark ? const Color(0xFF1E3A5F) : Colors.transparent),
            ),
            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          ),
        ),
      ],
    );
  }
}