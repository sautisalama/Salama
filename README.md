Sauti Salama ("Safe Voice" in Swahili) is a digital platform designed to provide critical services to survivors of sexual gender-based violence (SGBV) in Kenya. The platform includes a mobile progressive web application (PWA) and USSD service, offering a safe, anonymous, and accessible channel for survivors to report incidents and access legal, medical, and mental health support.

## Table of Contents
- [Project Overview](#project-overview)
- [Target Audience](#target-audience)
- [Project Goals](#project-goals)
- [Key Functionalities](#key-functionalities)
  - [Anonymous Reporting](#anonymous-reporting)
  - [Access to Mental Health Support](#access-to-mental-health-support)
  - [Access to Legal Guidance](#access-to-legal-guidance)
  - [Access to Health Resources](#access-to-health-resources)
  - [Support Services Matching](#support-services-matching)
  - [Community Support](#community-support)
  - [Analytics and Insights](#analytics-and-insights)
  - [Campaigns and Advocacy](#campaigns-and-advocacy)
  - [User Profile](#user-profile)
  - [Settings](#settings)
- [Technological Stack](#technological-stack)
- [Installation](#installation)
- [Usage](#usage)
- [AI Integration](#ai-integration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Sauti Salama aims to empower survivors of SGBV by providing them with the necessary tools and resources to report incidents and seek support. The platform ensures user safety, privacy, and accessibility across various devices and internet connection speeds. By leveraging modern technology, Sauti Salama strives to create a supportive environment for survivors, enabling them to access critical services and resources efficiently.

## Project Goals
- **User-Friendly Interface**: Design a user-friendly and intuitive interface that prioritizes user safety and privacy.
- **Accessibility**: Ensure the PWA is accessible on a variety of devices (phones, tablets) and internet connection speeds (slow or fast).
- **Efficient User Flow**: Create a clear and efficient user flow for reporting incidents and accessing resources.
- **Trust and Security**: Foster a sense of trust and security within the application through survivor empathy mapping and robust security measures.(Anonymity)
  
## Key Functionalities

### Anonymous Reporting
- **Feature**: Users can report SGBV incidents anonymously, with the option to include details if they choose.
- **Implementation**: A secure form that does not require personal identification information. The form allows users to describe the incident, select the type of violence, and provide any additional details they feel comfortable sharing.


### Access to Mental Health Support
- **Feature**: Users can connect with qualified mental health professionals.
- **Implementation**: A directory of mental health professionals is available, along with a booking system for appointments. Users can search for professionals based on their location, specialization, and availability.


### Access to Legal Guidance
- **Feature**: Lawyers are available to guide users on legal rights and processes.
- **Implementation**: A directory of pro bono lawyers is available, along with a system for scheduling legal consultations. Users can search for lawyers based on their expertise and availability.

### Access to Health Resources
- **Feature**: Users can access medical support and resources.
- **Implementation**: Information on nearby health facilities is provided, along with a booking system for medical appointments. Users can search for facilities based on their location and the type of medical support they need.

### Support Services Matching
- **Feature**: AI-driven matching of survivors with the best support services based on location and other criteria.
- **Implementation**: An AI model considers various factors such as location, survivor preferences, service provider specialties, and availability to provide accurate recommendations.

### Community Support
- **Feature**: Users can access a community of survivors, supporting each other as they heal.
- **Implementation**: A chat and forum system allows survivors to communicate and share experiences. Users can join discussion groups, participate in forums, and send private messages to other survivors.

### Analytics and Insights
- **Feature**: Administrators can view usage data and insights through a dashboard.
- **Implementation**: Real-time dashboards and advanced analytics tools provide detailed insights into platform usage, incident reports, and support service effectiveness.

### Campaigns and Advocacy
- **Feature**: Users can view ongoing campaigns and advocacy efforts, with details and participation options.
- **Implementation**: A dedicated page for campaigns and advocacy provides information on current initiatives, upcoming events, and ways to get involved.

### User Profile
- **Feature**: Users can view and edit their profile information.
- **Implementation**: A secure profile management system allows users to update their personal information, view their activity history, and manage their preferences.

### Settings
- **Feature**: Users can adjust notification preferences and privacy settings.
- **Implementation**: A settings page offers various customization options, including notification preferences, privacy settings, and account management.

## Technological Stack
- **Frontend**: HTML, CSS, JavaScript, Next (for PWA)
- **Backend**: Django, Django REST Framework
- **Database**: Superbase , Postgress
- **AI/ML**: Python, scikit-learn, TensorFlow
- **Hosting**: 

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Salama.git
    cd Salama
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Access the platform**: Open your web browser and navigate to `http://127.0.0.1:8000`.
2. **Report an incident**: Use the reporting form to submit an anonymous report.
3. **Access support services**: View matched support services based on your report.
4. **Manage your profile**: Edit your profile information and adjust settings.
5. **Join the community**: Participate in community chats and forums.

## Contributing
We welcome contributions from the community. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
