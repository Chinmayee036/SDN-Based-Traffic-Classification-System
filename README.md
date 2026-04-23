SDN Traffic Classification and Control using Mininet

📌 Project Overview
This project demonstrates the implementation of Software-Defined Networking (SDN) using Mininet and Ryu.
The system classifies network traffic into TCP, UDP, and ICMP protocols and applies control policies using OpenFlow.

🎯 Features
Classifies traffic into:
TCP
UDP
ICMP
Displays packet count and percentage distribution
Centralized control using SDN controller
Dynamic flow rule installation
(Optional) Traffic blocking between specific hosts

🏗️ Network Topology
h1 ----\
        \
h2 ----- s1 ---- Controller
        /
h3 ----/
h1, h2, h3 → Hosts
s1 → Switch

⚙️ Technologies Used
Python
Mininet
Ryu
OpenFlow
Ubuntu (Virtual Machine)

🚀 How to Run

1️⃣ Start Controller
python3 -m ryu.cmd.manager controller.py

2️⃣ Run Mininet Topology
sudo mn --custom topology.py --topo mytopo --controller=remote --switch ovsk,protocols=OpenFlow13

3️⃣ Generate Traffic (inside Mininet)
ICMP Traffic
h1 ping -c 3 10.0.0.2
TCP Traffic
h2 python3 -m http.server 80 &
h1 curl 10.0.0.2
UDP Traffic
h2 nc -u -l 5001 &
h1 bash -c "echo hi | nc -u 10.0.0.2 5001"

📊 Output
The controller displays traffic statistics:

--- Traffic Statistics ---
TCP: X packets (XX%)
UDP: X packets (XX%)
ICMP: X packets (XX%)

🧠 How It Works
Switch sends unknown packets to controller
Controller identifies protocol type
Updates statistics
Installs flow rules
Switch forwards or drops packets

🔒 Blocking Logic (if implemented)
Example:
Blocks traffic from h1 → h2
Demonstrates policy enforcement in SDN

📌 Key Concepts
Software-Defined Networking (SDN)
Centralized Control Plane
Flow Rules (Match + Action)
Packet Classification
Network Traffic Analysis

📈 Future Enhancements
Add graphical dashboard
Integrate machine learning
Expand to complex topologies
Real-time monitoring system

👩‍💻 Author
Chinmayee CM

📚 References
Mininet
Ryu
Computer Networking: A Top-Down Approach, Eighth Edition.
Data communications and networking by Forouzan, Behrouz A

