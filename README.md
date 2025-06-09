# Solar Energy Monitoring System

A modern solar energy monitoring system using ESP32 and Flask, deployed on Vercel. This system provides comprehensive monitoring of solar input, battery status, and load parameters.

## Features

### Solar Input Monitoring
- Voltage monitoring (19V DC - 200V DC)
- Current monitoring
- Power calculation
- Real-time data visualization

### Battery Monitoring
- Voltage monitoring (12V DC - 48V DC)
- Current monitoring
- Power calculation
- Total energy (Wh) tracking
- State of charge estimation

### Load Monitoring
- Current monitoring
- Power calculation
- Real-time consumption tracking

### Modern UI Features
- Responsive design for all devices
- Real-time data updates
- Interactive charts
- Beautiful gradient background
- Card-based layout with hover effects
- Modern typography using Inter font

## Components

- ESP32 microcontroller for sensor readings
- Flask backend API
- MongoDB database for data storage
- Modern web frontend with real-time updates
- Vercel deployment

## Hardware Requirements

- ESP32 development board
- Solar voltage sensor (voltage divider circuit for 19V-200V DC)
- Solar current sensor (ACS712 or similar)
- Battery voltage sensor (voltage divider circuit for 12V-48V DC)
- Battery current sensor
- Load current sensor
- Jumper wires
- Breadboard

## Setup Instructions

### ESP32 Setup

1. Install the required libraries in Arduino IDE:
   - WiFi.h
   - HTTPClient.h
   - ArduinoJson.h

2. Update the following in `esp32/energy_monitor.ino`:
   - WiFi credentials
   - API endpoint URL
   - Calibration factors for your sensors:
     - Solar voltage divider (19V-200V DC range)
     - Battery voltage divider (12V-48V DC range)
     - Current sensors

3. Upload the code to your ESP32

### Backend Setup

1. Create a MongoDB Atlas account and get your connection string

2. Create a `.env` file in the `api` directory with:
   ```
   MONGODB_URI=your_mongodb_connection_string
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend Setup

1. Update the API endpoint in `frontend/index.html` with your Vercel deployment URL

### Deployment

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy to Vercel:
   ```bash
   vercel
   ```

3. Set up environment variables in Vercel dashboard:
   - MONGODB_URI

## Usage

1. Power up the ESP32
2. Access the dashboard at your Vercel deployment URL
3. Monitor real-time solar, battery, and load parameters
4. View historical data in the interactive charts

## Technical Specifications

### Solar Input
- Voltage Range: 19V DC - 200V DC
- Current Range: 0-100A (configurable based on sensor)
- Update Rate: Every 5 seconds

### Battery
- Voltage Range: 12V DC - 48V DC
- Current Range: 0-100A (configurable based on sensor)
- Energy Tracking: Watt-hours (Wh)
- Update Rate: Every 5 seconds

### Load
- Current Range: 0-100A (configurable based on sensor)
- Power Calculation: Real-time
- Update Rate: Every 5 seconds

## Security Notes

- Keep your MongoDB connection string secure
- Use HTTPS for all communications
- Implement proper authentication for production use
- Regular security updates for ESP32 firmware
- Secure API endpoints with rate limiting 