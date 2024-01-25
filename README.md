# Moody's Scraper 🌐

## 🚀 Getting Started

Welcome to the Moody's Scraper project! This tool is designed to scrape, download, and index documents from specified sources for easy access and efficient searching.

### 🛠️ Development Environment 

- **Python Version**: 3.8+ (3.9+ recommended)
- **Recommended IDE**: Visual Studio Code or any IDE of your choice

#### Setup Instructions:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arunpshankar/Moodys-Demo.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Moodys-Demo
   ```

3. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Update Your PYTHONPATH**:
   ```bash
   export PYTHONPATH=$PYTHONPATH:.
   ```

### 6. Google Cloud Platform (GCP) Credentials
   Generate service account credentials for your GCP project, download the JSON key, and place it in the project's `credentials/` folder at the root directory.

### 📘 Steps to Start the Scraper

1. **Configure Settings**:
   - Start with the config YAML inside `config/`.
   - Ensure you have the project ID, credentials path, datastore ID, display name, and other necessary fields populated.

2. **Prepare Seed File**:
   - Use `seed.csv` to list companies and their entry point URLs for scraping.

3. **Run the Scraper**:
   ```bash
   python src/scrape/scraper.py
   ```
   - This collects PDF URLs and saves them in `data/output/pdf_urls.csv`.
   - For large seed lists, consider `async_scraper.py` for asynchronous operation.

### Steps to Download Documents from the Scraped PDF Links to Local

1. **Download PDFs**:
   ```bash
   python src/download/downloader.py
   ```
   - Use `async_downloader.py` for asynchronous downloading.

### Upload Local Documents to GCS 

1. **Upload to Google Cloud Storage (GCS)**:
   ```bash
   python src/upload/upload_docs.py
   ```
   - This script also generates `metadata.json` under `data/output/`, capturing company info for indexing.

### Indexing the Documents 

1. **Create Datastore**:
   ```bash
   python src/index/create_data_store.py
   ```

2. **Ingest Documents into Vertex AI Search**:
   ```bash
   python src/index/ingest_data.py
   ```

3. **Create Search Application**:
   ```bash
   python src/index/create_app.py
   ```

- Alternatively, for a smaller document count, run:
  ```bash
  python src/index/create_index.py
  ```

> **Note**: Depending on the number of documents, each indexing step might take time. It's recommended to run them sequentially.