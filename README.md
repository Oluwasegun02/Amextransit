# AmexTransit

Welcome to **AmexTransit**, a global logistics and transportation management website that provides efficient solutions for shipping, tracking, and logistics services. Our platform is designed to make logistics seamless, ensuring that your packages are always on the move and trackable with ease. 

You can visit the live site here: [AmexTransit](https://amextransit.onrender.com/)

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## About

AmexTransit is a robust logistics management system designed to connect global users with top-notch transportation and logistics services. We provide solutions ranging from multimodal transport operations to real-time tracking and logistics analytics. Our platform focuses on:

- Reducing shipping costs without compromising quality.
- Providing logistics solutions for individuals and businesses.
- Leveraging advanced technology for seamless tracking and management.

---

## Features

AmexTransit includes the following features:

1. **Tracking System**: 
   - Users can track the location and status of their shipments in real time.
   - Includes details such as origin, destination, current status, tariff, and more.

2. **User-Friendly Interface**:
   - Intuitive and responsive design for users on all devices (desktop, tablet, and mobile).

3. **About Us Page**:
   - Comprehensive information about AmexTransit’s mission, services, and vision.

4. **Real-Time Updates**:
   - Users receive live updates on shipment progress and status.

5. **Advanced Technology**:
   - Integrated with modern tools for transportation management systems (TMS) and inventory tracking.

6. **Tailored Services**:
   - Solutions customized for both individual and corporate clients.

---

## Technologies Used

This project was built with:

- **Backend**: Django (Python) - Powerful web framework for creating dynamic and scalable applications.
- **Frontend**: Tailwind CSS - For modern, responsive, and aesthetically pleasing designs.
- **Database**: SQLite - Lightweight, file-based database used for development.
- **Static Files**: Whitenoise - To serve static files in production.
- **Deployment**: Render - For hosting and managing the website.

---

## Installation

If you'd like to run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/amextransit.git
   cd amextransit
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Visit the app at `http://127.0.0.1:8000/`.

---

## Usage

### Tracking Your Shipment
1. Go to the **tracking page**.
2. Enter your tracking number in the search field.
3. Click on the "Track" button to view real-time updates about your shipment.

### About Us
Learn more about our services and mission on the **About Us** page.

---

## Environment Variables

To run this project in production, the following environment variables must be set:

- `SECRET_KEY`: The secret key for Django (ensure it's strong and kept private).
- `DEBUG`: Set to `False` in production.
- `DATABASE_URL`: The database connection URL (e.g., for PostgreSQL or SQLite).
- `RENDER_EXTERNAL_HOSTNAME`: Hostname provided by Render for deployment.

---

## Contributing

We welcome contributions to improve AmexTransit! Here's how you can get started:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any inquiries or support, please contact us:

- **Email**: support@amextransit.com
- **Website**: [AmexTransit](https://amextransit.onrender.com/)
- **Social Media**: Follow us on LinkedIn, Twitter, and Facebook.

---

Thank you for using AmexTransit! Let’s move your world, one shipment at a time. 🌍✈️🚢
