# Inventory Management System

## Overview

A Flask-based Inventory Management System that allows users to manage products through a REST API and a Command Line Interface (CLI).

The application supports CRUD operations, integrates with the OpenFoodFacts API, and includes automated tests using Pytest.

---

## Features

- View all inventory items
- View a single inventory item
- Add inventory items
- Update inventory items
- Delete inventory items
- Search products using OpenFoodFacts
- Add products from OpenFoodFacts into inventory
- Command Line Interface (CLI)
- Automated API tests

---

## Technologies Used

- Python
- Flask
- Requests
- Pytest
- OpenFoodFacts API

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd inventory-management-system
```

Install dependencies:

```bash
pipenv install
```

Activate virtual environment:

```bash
pipenv shell
```

---

## Running the API

```bash
python app.py
```

The API runs on:

```text
http://127.0.0.1:5000
```

---

## Running the CLI

Open a second terminal:

```bash
python cli.py
```

---

## Running Tests

```bash
pytest
```

---

## API Endpoints

### Inventory

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /inventory | Get all items |
| GET | /inventory/<id> | Get one item |
| POST | /inventory | Create item |
| PATCH | /inventory/<id> | Update item |
| DELETE | /inventory/<id> | Delete item |

### OpenFoodFacts

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /product/<barcode> | Lookup product |
| POST | /inventory/from-api/<barcode> | Add product to inventory |

---

## Example Barcode

```text
3017620422003
```

Returns product information for Nutella.

---

## Author

Rick Musyoki