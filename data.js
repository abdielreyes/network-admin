var data = {
    "nodes": [
        {
            "id": 1,
            "label": "R4",
            "group": "root_device"
        },
        {
            "id": 2,
            "label": "R2",
            "title": "<strong>Mgmt-IP:</strong><br>10.0.3.253<br><br><strong>Platform</strong>:<br> Cisco 7206VXR<br><br><strong>Version:</strong><br> Cisco IOS Software, 7200 Software (C7200-A3JK9S-M), Version 12.4(25g), RELEASE SOFTWARE (fc1)",
            "group": "attached_device"
        },
        {
            "id": 3,
            "label": "R3",
            "title": "<strong>Mgmt-IP:</strong><br>10.0.4.253<br><br><strong>Platform</strong>:<br> Cisco 7206VXR<br><br><strong>Version:</strong><br> Cisco IOS Software, 7200 Software (C7200-A3JK9S-M), Version 12.4(25g), RELEASE SOFTWARE (fc1)",
            "group": "attached_device"
        },
        {
            "id": 4,
            "label": "R1",
            "title": "<strong>Mgmt-IP:</strong><br>10.0.2.253<br><br><strong>Platform</strong>:<br> Cisco 7206VXR<br><br><strong>Version:</strong><br> Cisco IOS Software, 7200 Software (C7200-A3JK9S-M), Version 12.4(25g), RELEASE SOFTWARE (fc1)",
            "group": "attached_device"
        }
    ],
    "edges": [
        {
            "from": 1,
            "to": 2,
            "title": "from: FastEthernet1/0<br>to: FastEthernet1/0",
            "label": "",
            "value": 0,
            "font": {
                "align": "top"
            }
        },
        {
            "from": 1,
            "to": 3,
            "title": "from: FastEthernet2/0<br>to: FastEthernet1/0",
            "label": "",
            "value": 0,
            "font": {
                "align": "top"
            }
        },
        {
            "from": 1,
            "to": 4,
            "title": "from: FastEthernet0/0<br>to: FastEthernet1/0",
            "label": "",
            "value": 0,
            "font": {
                "align": "top"
            }
        }
    ]
}