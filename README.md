# Amazon Product Video Ad Script Generator API

A FastAPI-based backend service that generates video ad scripts from Amazon product URLs using AI. The service scrapes product information and uses Groq LLM to create engaging video ad scripts.

## Features

- Scrapes Amazon product pages for details
- Generates AI-powered video ad scripts
- Returns high-resolution product images
- RESTful API endpoints
- CORS enabled for frontend integration

## Prerequisites

- Python 3.8 or higher
- Chrome browser (for Selenium)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Backend
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

> Note: 
> - Get your Groq API key from [Groq Console](https://console.groq.com)
> - Get your Google API key from [Google Cloud Console](https://console.cloud.google.com)

## Running the Server

Start the FastAPI server with:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- API documentation: `http://localhost:8000/docs`
- Alternative documentation: `http://localhost:8000/redoc`

## Technology Stack

- FastAPI - Modern, fast web framework for building APIs
- Selenium - Web scraping
- BeautifulSoup4 - HTML parsing
- Langchain - LLM integration
- Groq - AI model provider
