## Permission Management System
# Project Overview
This is a web-based Permission Management System that facilitates managing permissions for students, faculty, admins, and security personnel. The system allows authorized users to log in and update permission statuses based on requests submitted by students. The platform is designed to streamline the process of managing permissions, including approval and rejection based on the submitted reasons.

# Features
User Authentication: Log in as a Student, Admin, Faculty, or Security Personnel.
Permission Requests: Students can submit requests for permissions (leave, special cases, etc.).
Permission Management: Admins and faculty can review and update the status of permission requests (Approve/Reject).
Status Tracking: Users can track the status of their requests in real-time.
Disabled Button After Update: Once a permission status is updated, the button becomes disabled and changes to "Status Updated."
Technologies Used
HTML/CSS: For creating the front-end user interface.
Django: Backend framework to handle requests, views, and database interactions.
SQLite: Database for managing user accounts and permission requests.


# Install Dependencies: Ensure that you have Python and Django installed on your system. Then, install any project dependencies:
pip install -r requirements.txt

# Run the Server: Navigate to the project directory and run the Django development server:
python manage.py runserver

# Access the System: Open your browser and navigate to http://127.0.0.1:8000/ to access the Permission Management System.

# Future Improvements
Add role-based authentication and advanced permission controls.
Implement email notifications for approved/rejected permissions.
Enhance the UI with better styling and mobile responsiveness.

# License
This project is licensed under the MIT License.
