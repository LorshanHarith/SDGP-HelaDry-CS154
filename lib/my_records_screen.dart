import 'package:flutter/material.dart';

class MyRecordsScreen extends StatelessWidget {
  const MyRecordsScreen({super.key});

  static const _demoBatches = [
    _BatchData(
      crop: 'Tomato',
      date: '11/17/2025',
      weightKg: 2,
      trays: 2,
      status: 'Active',
      duration: 'In progress',
    ),
    _BatchData(
      crop: 'Tomato',
      date: '11/17/2025',
      weightKg: 2,
      trays: 2,
      status: 'Active',
      duration: 'In progress',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    final totalBatches = _demoBatches.length;
    final activeBatches = _demoBatches.where((b) => b.status == 'Active').length;
    final completedBatches = totalBatches - activeBatches;
    final totalKg = _demoBatches.fold<double>(0, (sum, b) => sum + b.weightKg);

    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FA),
      appBar: AppBar(
        backgroundColor: const Color(0xFFAA33FF),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, color: Colors.white),
          onPressed: () => Navigator.pop(context),
        ),
        title: const Text('My Records', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(30),
          child: Padding(
            padding: const EdgeInsets.only(bottom: 12.0),
            child: Text('View all drying batches', style: TextStyle(color: Colors.white.withOpacity(0.9))),
          ),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // Stats Row
            GridView.count(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              crossAxisCount: 2,
              crossAxisSpacing: 12,
              mainAxisSpacing: 12,
              childAspectRatio: 1.4,
              children: [
                _StatsCard(label: 'Total Batches', value: '$totalBatches'),
                _StatsCard(label: 'Active', value: '$activeBatches'),
                _StatsCard(label: 'Completed', value: '$completedBatches'),
                _StatsCard(label: 'Total kg', value: totalKg.toStringAsFixed(1)),
              ],
            ),
            const SizedBox(height: 16),

            // Batch List
            Column(
              children: _demoBatches
                  .map((b) => Padding(
                        padding: const EdgeInsets.only(bottom: 12),
                        child: _BatchCard(batch: b),
                      ))
                  .toList(),
            ),
          ],
        ),
      ),
    );
  }
}

class _StatsCard extends StatelessWidget {
  final String label;
  final String value;

  const _StatsCard({required this.label, required this.value});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.black12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(value, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
          const SizedBox(height: 6),
          Text(label, style: const TextStyle(color: Colors.black54)),
        ],
      ),
    );
  }
}

class _BatchCard extends StatelessWidget {
  final _BatchData batch;

  const _BatchCard({required this.batch});

  @override
  Widget build(BuildContext context) {
    final isActive = batch.status.toLowerCase() == 'active';

    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: isActive ? Colors.green : Colors.black12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const CircleAvatar(child: Icon(Icons.local_florist, color: Colors.white), backgroundColor: Colors.green),
              const SizedBox(width: 10),
              Expanded(
                child: Text(batch.crop, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: isActive ? Colors.green : Colors.grey[200],
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Text(batch.status, style: TextStyle(color: isActive ? Colors.white : Colors.black87, fontSize: 12)),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Row(
            children: [
              const Icon(Icons.calendar_today, size: 16, color: Colors.black54),
              const SizedBox(width: 6),
              Text(batch.date, style: const TextStyle(color: Colors.black54)),
              const SizedBox(width: 16),
              const Icon(Icons.scale, size: 16, color: Colors.black54),
              const SizedBox(width: 6),
              Text('${batch.weightKg} kg', style: const TextStyle(color: Colors.black54)),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            children: [
              const Icon(Icons.layers, size: 16, color: Colors.black54),
              const SizedBox(width: 6),
              Text('${batch.trays} trays', style: const TextStyle(color: Colors.black54)),
            ],
          ),
          const SizedBox(height: 8),
          Text('Duration: ${batch.duration}', style: const TextStyle(color: Colors.black54)),
        ],
      ),
    );
  }
}

class _BatchData {
  final String crop;
  final String date;
  final double weightKg;
  final int trays;
  final String status;
  final String duration;

  const _BatchData({
    required this.crop,
    required this.date,
    required this.weightKg,
    required this.trays,
    required this.status,
    required this.duration,
  });
}
