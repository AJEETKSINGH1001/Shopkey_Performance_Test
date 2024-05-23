Locust Performance Testing
This repository contains a Locust setup for performing end-to-end performance testing on the website https://test0106store1a.goshopkey.com.

Setup and Installation
Clone the Repository:
Clone this repository to your local machine using:
Install Locust:
Ensure you have Python 3.7 or above. Install Locust using:
Running the Tests
Start Locust:
Run Locust with the command:
locust -f locustfile.py --host=https://test0106store1a.goshopkey.com
Open Locust Web Interface:
Open your browser and go to http://localhost:8089.

Configure and Start Test:

Set the number of users to simulate (e.g., 100 users).
Set the spawn rate (e.g., 10 users per second).
Click "Start swarming" to begin the load test.
Customizing Tests
Modify locustfile.py to customize user behavior and tasks to reflect typical user interactions on your site.

Analyzing Results
Requests per Second (RPS): Monitor how many requests per second your site handles.
Response Time: Check server response times.
Failures: Observe any errors or failed requests.
Charts and Graphs: Use the Locust web interface for visual insights into the performance metrics.
Contributing
Contributions are welcome! Feel free to fork this repository, make enhancements, and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
