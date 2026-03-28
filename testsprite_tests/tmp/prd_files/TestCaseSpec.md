**Chapter 2 : Testing**

**2.1. Chapter Introduction**

The HelaDry system implementation was covered in detail in the previous chapter. This chapter provides a comprehensive overview of the testing performed on the HelaDry solar-powered IoT dehydrator companion application. The functional and non-functional requirements that were identified in the requirements specification chapter will be validated here through test cases. This chapter first explains what will be tested and why, and then offers a analysis through test case tables. Before the prototype is put for review, the objective of this section is to validate its requirements.

**2.2. Testing Criteria**

Software development projects must include product testing to ensure that the functionality and performance of the final product adhere to the specified functional and non-functional requirements. This part involves comparing the functionality of the HelaDry prototype against the requirements set out during the requirement phase. Testing was carried out to access the system\'s functionality, identify any flaws or problems, and appyly the necessary solutions to fix it

The HelaDry application was tested across its two primary operational modes: Online Mode (Wi-Fi and Firebase connectivity) and Offline Mode (Bluetooth BLE). All core user flows were validated --- from the splash screen and authentication, through device pairing and Wi-Fi provisioning, to the dashboard, manual controls, batch management, and settings. Since the system interacts with real embedded hardware testing also covered the firmware integration layer including BLE characteristic communication and Firebase Realtime Database synchronization.

Hence, while the system was being tested, bugs were fixed and performance was enhanced. As a result, the main goal of product testing was to ensure the item is in the best possible condition and complies with the required functionality and performance criteria. Each test case was evaluated with a binary Pass/Fail status to clearly measure whether the system implementation meets its defined requirements.

**2.3. Testing Functional Requirements**

The table below presents the functional test cases derived from the HelaDry system\'s functional requirements. These cover the complete user journey from application launch and authentication, through device pairing, real-time monitoring, batch management, and manual controls.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Test Case Number</th>
<th>Test Case Description</th>
<th>Expected Outcome</th>
<th>Actual Outcome</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FR1</td>
<td>User can launch the HelaDry app and view the splash screen</td>
<td><p>splash screen appears</p>
<p>App logo displayed</p>
<p>2.2 second delay</p>
<p>Auto-redirect on login check</p></td>
<td><p>Splash screen loads with HelaDry logo</p>
<p>Redirects logged-in users to Connection Mode</p>
<p>Redirects new users to Login Page</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>FR2</td>
<td>User can register a new account and log in</td>
<td><p>Create account form with validation</p>
<p>Email and password fields</p>
<p>Password confirm matching</p>
<p>Login with credentials</p></td>
<td><p>Account creation validates all fields</p>
<p>Password mismatch shows error</p>
<p>Successful login redirects to Connection Mode page</p></td>
<td>Pass</td>
</tr>
<tr class="odd">
<td>FR3</td>
<td>User can select Online (Wi-Fi) or Offline (BLE) connection mode</td>
<td><p>Connection Mode page appears after login</p>
<p>Online Mode option available</p>
<p>Offline Mode option available</p></td>
<td><p>Connection Mode selection screen loads</p>
<p>Online and Offline mode cards are displayed</p>
<p>User can tap either mode to proceed</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>FR4</td>
<td>User can pair the HelaDry device via Bluetooth BLE</td>
<td><p>BLE scan starts on Pair Device page</p>
<p>Devices listed with RSSI and signal quality</p>
<p>Connect button available</p>
<p>Pairing success confirmation page shown</p></td>
<td><p>Device scan runs and lists nearby HELADRY-XXXX devices</p>
<p>User can tap Connect</p>
<p>Pair Success page confirms device pairing</p></td>
<td>Pass</td>
</tr>
<tr class="odd">
<td>FR5</td>
<td>User can configure Wi-Fi credentials for the dehydrator (Online Mode)</td>
<td><p>Step 1: Wi-Fi network scan and selection</p>
<p>Step 2: Password entry with toggle</p>
<p>Step 3: Confirmation with saved network display</p></td>
<td><p>Wi-Fi networks listed with signal strength</p>
<p>Password entered and submitted</p>
<p>Confirmation page shows connected network name</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>FR6</td>
<td>User can view live sensor metrics on the Dashboard</td>
<td><p>Dashboard displays real-time metrics</p>
<p>Temperature, Humidity, Fan Speed, Heater, Battery, Solar shown</p></td>
<td><p>Dashboard loads with 2x3 metrics grid</p>
<p>All sensor values displayed with icons and units</p>
<p>Online/Offline connection indicator shown</p></td>
<td>Pass</td>
</tr>
<tr class="odd">
<td>FR7</td>
<td>User can start a new drying batch</td>
<td><p>Start New Batch page accessible from Dashboard</p>
<p>Crop selector (7 crops)</p>
<p>Tray count and weight input</p>
<p>Auto-fills recommended temperature</p></td>
<td><p>Batch page loads with crop selection</p>
<p>Dropdown shows all 7 supported crops</p>
<p>Recommended temperature auto-populated</p>
<p>Batch session begins on submit</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>FR8</td>
<td>User can manually control the dehydrator (fan, heater, temperature)</td>
<td><p>Fan speed slider 0-100%</p>
<p>Target temperature slider 30-80°C</p>
<p>Heater toggle ON/OFF</p>
<p>Emergency Stop button with confirmation dialog</p></td>
<td><p>Fan speed slider applies on 'Apply' button press</p>
<p>Heater toggles immediately</p>
<p>Emergency Stop halts all operations and shows confirmation</p></td>
<td>Pass</td>
</tr>
</tbody>
</table>

**2.4. Testing Non-Functional Requirements**

The following table presents the non-functional test cases for the HelaDry system. These tests validate the system\'s performance, usability, reliability, accuracy, and compatibility.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 28%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>Test Case No.</th>
<th>Test Case Description</th>
<th>Test Case Condition</th>
<th>Expected Outcome</th>
<th>Actual Outcome</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NFR1</td>
<td>Accuracy</td>
<td>Sensor data readings from the ESP32 firmware</td>
<td><p>Sensor readings are accurate and consistent</p>
<p>Temperature and humidity values match expected ranges</p></td>
<td><p>The app displays sensor data streamed via BLE/Firebase</p>
<p>Calibration offsets (temp_offset, humidity_offset) configurable in Settings</p>
<p>Values align with expected ranges during testing</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>NFR2</td>
<td>Performance</td>
<td>Flutter mobile app on Android and iOS devices</td>
<td><p>App loads within 3 seconds</p>
<p>Screen transitions are smooth</p>
<p>No lag during real-time metric updates</p></td>
<td><p>App launches and navigates without noticeable delay</p>
<p>Fade+slide page animations execute within 250ms</p>
<p>Dashboard metrics update in real-time</p></td>
<td>Pass</td>
</tr>
<tr class="odd">
<td>NFR3</td>
<td>Usability</td>
<td>User-friendly GUI design with Light/Dark mode and responsive layout</td>
<td><p>Users can tap buttons, navigate screens, and control the device with ease</p>
<p>UI adapts to light and dark themes</p></td>
<td><p>Large, clearly labelled buttons throughout the app</p>
<p>Light and Dark themes tested and functional All primary actions (start batch, emergency stop, controls) are accessible within 2 taps from Dashboard</p></td>
<td>Pass</td>
</tr>
<tr class="even">
<td>NFR4</td>
<td>Reliability</td>
<td>Offline BLE mode and Online Wi-Fi/Firebase mode</td>
<td><p>App maintains connectivity and data flow in both modes</p>
<p>App does not crash during mode switching or data updates</p></td>
<td><p>BLE Offline mode functions without internet</p>
<p>Online mode syncs data via Firebase RTDB</p>
<p>DeviceTransport singleton abstracts both modes reliably</p>
<p>Emergency Stop tested to halt all outputs correctly</p></td>
<td>Pass</td>
</tr>
<tr class="odd">
<td>NFR5</td>
<td>Compatibility</td>
<td>Compatibility testing on Android and iOS physical devices</td>
<td><p>App should be compatible with Android and iOS platforms</p>
<p>App runs on different screen sizes</p></td>
<td><p>App built using Flutter cross-platform framework</p>
<p>Tested on Android (physical device) and iOS simulator</p>
<p>Responsive layout adapts to different screen dimensions</p>
<p>Light and Dark themes verified on both platforms</p></td>
<td>Pass</td>
</tr>
</tbody>
</table>

U

Usability Testing

**2.7.1 Introduction**

Usability testing was conducted to evaluate how easily end users can interact with the HelaDry system, which consists of an IoT-based solar dehydration device and a mobile application. The primary objective was to ensure that farmers and general users can efficiently operate the system without requiring technical expertise.

**2.7.2 Objectives of Usability Testing**

- To evaluate the ease of use of the mobile application

- To assess user interaction with the IoT device controls

- To identify any difficulties faced by users

- To ensure the system is user-friendly for non-technical users (e.g., farmers)

- To improve overall user experience and satisfaction

![](media/image1.jpeg){width="2.5166666666666666in" height="4.866666666666666in"}![](media/image2.jpeg){width="2.591666666666667in" height="4.916666666666667in"}

**2.7.3 Effectiveness and Efficiency**

Effectiveness and efficiency were evaluated to determine how accurately and quickly users could complete tasks using the HelaDry system.

- Users were able to successfully complete key tasks such as connecting to the IoT device, monitoring data, and controlling the dehydration process

- The system produced accurate real-time temperature and humidity readings

- Tasks were completed within a short time with minimal effort

- The application required only a few steps to perform main functions, improving speed and usability

![](media/image3.png){width="3.1166666666666667in" height="6.133333333333334in"}![](media/image4.png){width="2.925in" height="6.191666666666666in"}  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![](media/image5.png){width="3.025in" height="6.291666666666667in"}

**2.7.3 Accessibility and Design Principles**

The HelaDry mobile application was designed with accessibility and inclusive design as foundational priorities, ensuring that the system is usable by a broad range of users, including farmers in rural Sri Lanka who may have limited technical literacy or experience with mobile applications.

**2.7.4 Light and Dark Mode Support**

The application supports both light and dark themes, allowing users to switch between modes based on their personal preference or ambient lighting conditions. This is particularly relevant in outdoor agricultural environments where screen visibility under direct sunlight is a concern. Dark mode also reduces eye strain in low-light conditions and can extend battery life on OLED-based devices, which is beneficial given the system\'s solar-powered context.

**2.7.5 Colour Psychology and Visual Design**

The colour palette was selected through careful research into colour psychology and its effects on user perception and behaviour. Warm, earthy tones were incorporated to reflect the agricultural context of the application and to create a sense of familiarity for the target user group. High-contrast colour combinations were used across both themes to ensure readability and to meet standard visual accessibility guidelines. 

**2.7.6 Typography and Readability**

Font sizes and weights were chosen to ensure clear legibility across a variety of screen sizes and resolutions. Labels, button text, and metric values are prominently displayed to minimise cognitive load, which aligns with Nielsen\'s (1994) usability heuristic of recognition over recall. The interface avoids dense blocks of text, favouring iconographic representations and concise labels to support users with lower literacy levels.

**2.7.7 Inclusive and User-Centred Layout**

The application follows a grid-based layout that organises information consistently across all screens. Primary actions such as starting a batch, triggering an emergency stop, and switching control modes are placed within two taps of the main dashboard, reducing navigation complexity. Large, clearly labelled buttons and interactive elements ensure the application is operable by users with limited fine motor precision or those unfamiliar with touchscreen interfaces.

**2.7.8 Responsive Design **

The Flutter framework\'s cross-platform rendering engine ensures that the application\'s layout adapts consistently across devices with varying screen dimensions, including smaller-budget Android handsets commonly used in rural settings. This ensures a uniform user experience without requiring device-specific design adjustments.

![](media/image6.jpeg){width="2.625in" height="5.016666666666667in"}

![](media/image7.png){width="2.7333333333333334in" height="5.108333333333333in"}

**Test Cases**

| ID  | Description                                | Expected Outcome                        | Status |
|-----|--------------------------------------------|-----------------------------------------|--------|
| 01  | Connect app to IoT device                  | App successfully connects to IoT device | PASS   |
| 02  | Real-time temperature & humidity displayed | Data displayed correctly                | PASS   |
| 03  | Start dehydration process                  | Dehydration process begins              | PASS   |
| 04  | Stop dehydration process                   | Dehydration stops immediately           | PASS   |
| 05  | Open progress/status screen                | Progress visible in real-time           | PASS   |
| 06  | New user uses app without help             | Users completed tasks with minimal help | PASS   |

2.8 Compatibility Testing

| Requirement | Minimum                        | Recommended            |
|-------------|--------------------------------|------------------------|
| OS          | Android 8.0                    | Android 10 or higher   |
| RAM         | 2GB                            | 4GB                    |
| Storage     | 16GB (with atleast 200mb free) | 32GB                   |
| Display     | 720 x 1280                     | 1080 x 1920 or higher  |

![](media/image8.jpeg){width="6.5in" height="3.625in"}

![](media/image9.jpeg){width="6.5in" height="3.2375in"}

Compatibility testing was conducted to ensure that the HelaDry mobile application operates smoothly across a wide range of devices, operating systems, and network conditions. This process involved testing the application on multiple smartphone models with different screen sizes, resolutions, and hardware capabilities to ensure consistent performance and usability.

The application was evaluated on various Android devices, including the Redmi Note 12S, Oppo A17, and Samsung A12. These devices represent different performance levels and display configurations, allowing the team to verify that the application remains responsive and visually consistent across both mid-range and budget smartphones. Testing across these devices ensured that key functionalities such as navigation, data display, and user interactions---worked efficiently without crashes or delays.

**2.7.9  Summary**

This chapter outlines the essential testing processes carried out to ensure the overall quality and reliability of the application. Functional testing was performed to verify that all system features operate according to the specified requirements. Unit testing was implemented at an early stage to identify and resolve errors within individual components, improving code reliability.

In addition, usability testing focused on evaluating the user interface and overall user experience, ensuring the application is intuitive and easy to navigate. Performance testing assessed the system's responsiveness, speed, and stability under different conditions. Finally, compatibility testing ensured that the application functions effectively across a variety of devices, screen sizes, and operating system versions, providing a consistent experience for all users.
