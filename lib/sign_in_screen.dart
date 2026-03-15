import 'package:flutter/material.dart';

class SignInScreen extends StatefulWidget {
  const SignInScreen({super.key});

  @override
  State<SignInScreen> createState() => _SignInScreenState();
}

class _SignInScreenState extends State<SignInScreen> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool _obscurePassword = true;

  void _togglePassword() {
    setState(() {
      _obscurePassword = !_obscurePassword;
    });
  }

  void _signIn() {
    // TODO: Add authentication logic
    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Sign in pressed')));
  }

  void _createAccount() {
    // TODO: Navigate to register page
    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Create account pressed')));
  }

  void _forgotPassword() {
    // TODO: Add password recovery
    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Forgot password pressed')));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1A1A1A),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 32),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const SizedBox(height: 16),
                const Text('Sign in', style: TextStyle(color: Colors.white70, fontSize: 18)),
                const SizedBox(height: 16),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 28),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [
                      BoxShadow(color: Colors.black.withOpacity(0.14), blurRadius: 20, offset: const Offset(0, 8)),
                    ],
                  ),
                  child: Column(
                    children: [
                      Container(
                        width: 72,
                        height: 72,
                        decoration: BoxDecoration(
                          color: const Color(0xFFE9F3EA),
                          shape: BoxShape.circle,
                        ),
                        child: const Center(
                          child: Icon(Icons.wb_sunny, color: Color(0xFF13B546), size: 36),
                        ),
                      ),
                      const SizedBox(height: 14),
                      const Text('Dehydrator Assistant', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
                      const SizedBox(height: 6),
                      const Text('Smart Solar Drying for Farmers', style: TextStyle(color: Colors.black54)),
                      const SizedBox(height: 24),

                      // Avatar placeholder
                      const CircleAvatar(
                        radius: 38,
                        backgroundColor: Color(0xFFF1F3F4),
                        child: Icon(Icons.person, size: 44, color: Colors.black26),
                      ),
                      const SizedBox(height: 24),

                      // Email / Phone field
                      TextField(
                        controller: _emailController,
                        keyboardType: TextInputType.emailAddress,
                        decoration: InputDecoration(
                          labelText: 'Phone Number or Email',
                          hintText: 'Enter phone or email',
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                          filled: true,
                          fillColor: const Color(0xFFF7F7F7),
                        ),
                      ),
                      const SizedBox(height: 16),

                      // Password field
                      TextField(
                        controller: _passwordController,
                        obscureText: _obscurePassword,
                        decoration: InputDecoration(
                          labelText: 'Password',
                          hintText: 'Enter password',
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                          filled: true,
                          fillColor: const Color(0xFFF7F7F7),
                          suffixIcon: IconButton(
                            icon: Icon(_obscurePassword ? Icons.visibility : Icons.visibility_off),
                            onPressed: _togglePassword,
                          ),
                        ),
                      ),
                      const SizedBox(height: 8),

                      Align(
                        alignment: Alignment.centerRight,
                        child: TextButton(
                          onPressed: _forgotPassword,
                          child: const Text('Forgot Password?', style: TextStyle(color: Color(0xFF13B546))),
                        ),
                      ),
                      const SizedBox(height: 12),

                      SizedBox(
                        width: double.infinity,
                        height: 50,
                        child: ElevatedButton(
                          onPressed: _signIn,
                          style: ElevatedButton.styleFrom(
                            backgroundColor: const Color(0xFF13B546),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                          ),
                          child: const Text('Log In', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                        ),
                      ),
                      const SizedBox(height: 12),

                      TextButton(
                        onPressed: _createAccount,
                        child: const Text('New User? Create Account', style: TextStyle(color: Color(0xFF13B546))),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
