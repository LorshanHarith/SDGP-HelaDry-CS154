#!/usr/bin/env python3
"""
Test summary generator for HelaDry Postman automation.
This script analyzes Newman JSON reports and generates a comprehensive summary.
"""

import json
import sys
import os
from datetime import datetime

def load_json_file(filepath):
    """Load JSON data from file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {filepath}: {e}")
        return None

def analyze_test_results(data, test_type):
    """Analyze test results from Newman JSON data."""
    if not data or 'run' not in data:
        return {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'total_requests': 0,
            'failed_requests': 0,
            'success_rate': 0,
            'avg_response_time': 0,
            'total_duration': 0
        }
    
    run_data = data['run']
    executions = run_data.get('executions', [])
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    total_requests = len(executions)
    failed_requests = 0
    response_times = []
    total_duration = 0
    
    for execution in executions:
        # Count tests
        test_events = execution.get('assertions', [])
        total_tests += len(test_events)
        
        # Count passed/failed tests
        for test in test_events:
            if test.get('passed', False):
                passed_tests += 1
            else:
                failed_tests += 1
        
        # Count failed requests
        if execution.get('error'):
            failed_requests += 1
        
        # Collect response times
        response = execution.get('response', {})
        if response and 'responseTime' in response:
            response_times.append(response['responseTime'])
        
        # Calculate duration
        if 'item' in execution and 'event' in execution:
            # This is a simplified duration calculation
            total_duration += response.get('responseTime', 0)
    
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    avg_response_time = (sum(response_times) / len(response_times)) if response_times else 0
    
    return {
        'total_tests': total_tests,
        'passed_tests': passed_tests,
        'failed_tests': failed_tests,
        'total_requests': total_requests,
        'failed_requests': failed_requests,
        'success_rate': round(success_rate, 2),
        'avg_response_time': round(avg_response_time, 2),
        'total_duration': round(total_duration, 2)
    }

def generate_summary_report(backend_file, frontend_file, output_file):
    """Generate a comprehensive test summary report."""
    print("📋 Generating test summary report...")
    
    # Load test data
    backend_data = load_json_file(backend_file)
    frontend_data = load_json_file(frontend_file)
    
    # Analyze results
    backend_results = analyze_test_results(backend_data, "Backend")
    frontend_results = analyze_test_results(frontend_data, "Frontend")
    
    # Calculate totals
    total_tests = backend_results['total_tests'] + frontend_results['total_tests']
    total_passed = backend_results['passed_tests'] + frontend_results['passed_tests']
    total_failed = backend_results['failed_tests'] + frontend_results['failed_tests']
    total_requests = backend_results['total_requests'] + frontend_results['total_requests']
    total_failed_requests = backend_results['failed_requests'] + frontend_results['failed_requests']
    
    overall_success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    
    # Generate report
    report = f"""{'='*60}
           HELADRY POSTMAN TEST SUMMARY
{'='*60}

📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🎯 Test Type: Backend API + Frontend Integration
🧪 Automation: Fully Automated Postman Tests

{'='*60}
                    BACKEND API TESTS
{'='*60}

📊 Test Statistics:
   • Total Tests: {backend_results['total_tests']}
   • Passed: {backend_results['passed_tests']} ✅
   • Failed: {backend_results['failed_tests']} ❌
   • Success Rate: {backend_results['success_rate']}% {'✅' if backend_results['success_rate'] >= 80 else '⚠️'}

🌐 Request Statistics:
   • Total Requests: {backend_results['total_requests']}
   • Failed Requests: {backend_results['failed_requests']} {'✅' if backend_results['failed_requests'] == 0 else '⚠️'}
   • Average Response Time: {backend_results['avg_response_time']}ms {'✅' if backend_results['avg_response_time'] < 3000 else '⚠️'}

⏱️ Performance:
   • Total Duration: {backend_results['total_duration']}ms
   • API Health: {'✅ Healthy' if backend_results['success_rate'] >= 90 and backend_results['failed_requests'] == 0 else '⚠️ Needs Attention'}

{'='*60}
               FRONTEND INTEGRATION TESTS
{'='*60}

📊 Test Statistics:
   • Total Tests: {frontend_results['total_tests']}
   • Passed: {frontend_results['passed_tests']} ✅
   • Failed: {frontend_results['failed_tests']} ❌
   • Success Rate: {frontend_results['success_rate']}% {'✅' if frontend_results['success_rate'] >= 80 else '⚠️'}

🌐 Request Statistics:
   • Total Requests: {frontend_results['total_requests']}
   • Failed Requests: {frontend_results['failed_requests']} {'✅' if frontend_results['failed_requests'] == 0 else '⚠️'}
   • Average Response Time: {frontend_results['avg_response_time']}ms {'✅' if frontend_results['avg_response_time'] < 3000 else '⚠️'}

📱 Mobile UX Performance:
   • Total Duration: {frontend_results['total_duration']}ms
   • Flutter Compatibility: {'✅ Compatible' if frontend_results['success_rate'] >= 90 and frontend_results['failed_requests'] == 0 else '⚠️ Needs Review'}

{'='*60}
                      OVERALL SUMMARY
{'='*60}

🎯 Overall Statistics:
   • Total Tests: {total_tests}
   • Total Passed: {total_passed} ✅
   • Total Failed: {total_failed} ❌
   • Overall Success Rate: {round(overall_success_rate, 2)}% {'✅ Excellent' if overall_success_rate >= 95 else '✅ Good' if overall_success_rate >= 85 else '⚠️ Needs Improvement' if overall_success_rate >= 70 else '❌ Critical Issues'}

🚀 System Health:
   • Backend API: {'✅ Healthy' if backend_results['success_rate'] >= 90 and backend_results['failed_requests'] == 0 else '⚠️ Monitor Closely'}
   • Frontend Integration: {'✅ Healthy' if frontend_results['success_rate'] >= 90 and frontend_results['failed_requests'] == 0 else '⚠️ Monitor Closely'}
   • Overall Status: {'🎉 Production Ready!' if overall_success_rate >= 90 and total_failed_requests == 0 else '⚠️ Review Required' if overall_success_rate >= 75 else '❌ Critical Issues Found'}

{'='*60}
                        RECOMMENDATIONS
{'='*60}

"""
    
    # Add recommendations based on results
    if overall_success_rate >= 95:
        report += """✅ EXCELLENT: All tests passing! System is ready for production.
   • Continue monitoring performance metrics
   • Consider adding more edge case tests
   • Schedule regular automated test runs
"""
    elif overall_success_rate >= 85:
        report += """✅ GOOD: Minor issues detected.
   • Review failed tests in the detailed reports
   • Check server performance under load
   • Verify Firebase authentication setup
"""
    elif overall_success_rate >= 70:
        report += """⚠️  NEEDS ATTENTION: Several test failures detected.
   • Review backend server logs for errors
   • Check database connectivity
   • Verify Firebase project configuration
   • Test network connectivity and firewall settings
"""
    else:
        report += """❌ CRITICAL: Major issues detected.
   • Check backend server status and logs
   • Verify all dependencies are installed
   • Review API endpoint implementations
   • Check authentication and authorization setup
"""
    
    if backend_results['avg_response_time'] > 3000:
        report += """
   ⚠️  Backend response times are slow (>3s)
      • Consider optimizing database queries
      • Check server resource usage
      • Review API endpoint performance
"""
    
    if frontend_results['avg_response_time'] > 3000:
        report += """
   ⚠️  Frontend response times are slow (>3s)
      • Mobile app may have poor UX
      • Consider implementing caching
      • Review API response formats
"""
    
    report += f"""

📁 Report Files Generated:
   • Backend Tests: {os.path.basename(backend_file)}
   • Frontend Tests: {os.path.basename(frontend_file)}
   • Summary Report: {os.path.basename(output_file)}

🔧 Next Steps:
   1. Review detailed HTML reports for specific failures
   2. Check backend server logs for errors
   3. Verify Firebase authentication setup
   4. Run tests again after fixes
   5. Consider setting up CI/CD automation

{'='*60}
                     END OF REPORT
{'='*60}
"""
    
    # Write report to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Summary report generated: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Failed to write summary report: {e}")
        return False

def main():
    """Main function to run the test summary generator."""
    if len(sys.argv) != 4:
        print("Usage: python generate_test_summary.py <backend_json> <frontend_json> <output_txt>")
        print("Example: python generate_test_summary.py backend_tests.json frontend_tests.json summary.txt")
        sys.exit(1)
    
    backend_file = sys.argv[1]
    frontend_file = sys.argv[2]
    output_file = sys.argv[3]
    
    success = generate_summary_report(backend_file, frontend_file, output_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()