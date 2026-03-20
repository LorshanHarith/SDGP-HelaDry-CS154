# Local Commit Plan

The following is a list of exactly 32 organized, logical, consecutive commits that demonstrate the integration timeline. You can run these manually using standard `git commit -m` commands grouping the files incrementally, or apply them via a script.

1. `chore: initialize dependencies for flutter reactive ble and firebase`
2. `chore: configure android manifest for bluetooth and location permissions`
3. `chore: configure ios info plist for bluetooth usage descriptions`
4. `feat(firmware): extract mac address to generate dynamic ble device name`
5. `refactor(firmware): replace hardcoded device id with dynamic ble name`
6. `feat(firmware): expose dynamic ble name in telemetry characteristic payload`
7. `feat(firmware): setup dedicated ack characteristic for command responses`
8. `feat(firmware): implement scan_wifi command handler inside ble callbacks`
9. `feat(firmware): execute async wifi scan and serialize ssids to json`
10. `feat(firmware): broadcast wifi scan json results via ble ack characteristic`
11. `feat(firmware): update set_wifi_creds command to store and attempt connection`
12. `fix(firmware): ensure firebase initializes automatically after late wifi provisioning`
13. `feat(firmware): add temperature and humidity offset tracking variables`
14. `feat(firmware): apply sensor offsets to bme280 telemetry calculation`
15. `feat(firmware): update set_manual_outputs to accept configuration offsets`
16. `feat(firmware): sync runtime configuration offsets from firebase /config node`
17. `feat(flutter): create unified device state model for transport abstraction`
18. `feat(flutter): implement native bel device service with scanner and connection`
19. `feat(flutter): parse incoming ble characteristic stream into device state model`
20. `feat(flutter): map ble ack responses into dedicated acknowledgment stream`
21. `feat(flutter): create firebase device service for rtdb telemetry stream`
22. `feat(flutter): implement device transport singleton to orchestrate ble and wi-fi`
23. `refactor(flutter): wire pair device page to real ble network scanner`
24. `refactor(flutter): establish connection from pair page to hardware mac address`
25. `refactor(flutter): wire wi-fi setup step 2 to trigger hardware scan_wifi command`
26. `refactor(flutter): parse wi-fi setup ble ack stream into network list ui`
27. `refactor(flutter): wire wi-fi setup step 3 to dispatch set_wifi_creds over ble`
28. `refactor(flutter): replace mock metrics in dashboard with device transport stream`
29. `refactor(flutter): dynamically map session progress and active states in dashboard ui`
30. `refactor(flutter): wire manual controls page to send set_manual_outputs via transport`
31. `refactor(flutter): wire emergency stop to broadcast stop command hardware-wide`
32. `refactor(flutter): wire start new batch page to trigger start_session command`
33. `docs: generate implementation summary, test checklist, and security notes`
