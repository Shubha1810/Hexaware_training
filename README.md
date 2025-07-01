
# 🕵️‍♂️ **Crime Analysis and Reporting System (C.A.R.S.)**

## 📌 **Project Overview**

**Crime Analysis and Reporting System (C.A.R.S.)** is a **Python-based Command-Line Interface (CLI)** application built to help **law enforcement agencies** and **crime analysts** systematically record, manage, search, and analyze crime-related data.

Key features include:

* Full **CRUD operations**
* **Geolocation-based** data capture
* **Report generation**
* **Case management system**
* CLI-based interaction with clean tabular output


## 🗂️ **Project Structure**


cars_project/
│
├── dao/                            # Business logic and service layer
│   ├── crime_analysis_service_impl.py
│   ├── icrime_analysis_service.py
│
├── database/                       # SQL schema and data records
│   ├── schema/
│   └── records/
│
├── entity/                         # Data model classes
│   ├── agency.py
│   ├── case.py
│   ├── evidence.py
│   ├── incident.py
│   ├── officer.py
│   ├── report.py
│   ├── suspect.py
│   └── victim.py
│
├── exception/                      # Custom exceptions
│   └── incident_not_found_exception.py
│
├── main/                           # Main application entry point
│   └── main_module.py
│
├── test/                           # Unit test cases
│   └── test_crime_analysis.py
│
├── util/                           # Utility modules and configs
│   ├── db_conn_util.py
│   ├── db_property_util.py
│   ├── geocode_util.py
│   └── db_config.properties
│
└── .venv/                          # Virtual environment (optional)



## 🔄 **Major Functional Flow**

### 1️⃣ **Incident Recording (with Geolocation)**

* Prompts user for:

  * Incident Type
  * Date (defaults to today if left blank)
  * Location (e.g., Mumbai, Andheri)
* Automatically fetches **Latitude & Longitude** using `GeoCodeUtil`.
* Requires existing entries of:

  * Victim
  * Suspect
  * Law Enforcement Agency


### 2️⃣ **Data Entry Modules**

Supports adding:

* ✅ Victim details
* ✅ Suspect details
* ✅ Police officer details (linked to agencies)
* ✅ Law enforcement agencies
* ✅ Evidence (linked to incidents)

**Input validation:**

* Date format: `YYYY-MM-DD`
* Email checks:

  * `@gmail.com` → for victims/suspects/officers
  * `@police.gov` → for agencies

### 3️⃣ **Case Management**

* Create new case with a **description** and **linked incidents**
* Update or view existing case details
* View all cases with timestamps


### 4️⃣ **Reporting Capabilities**

Generate incident/case reports:

* 📅 **Today**
* 🗓️ **This Month**
* 📆 **This Year**
* 📍 **Custom Date Range**
* 🧾 **Specific Month & Year**


### 5️⃣ **Search & Query Options**

* 🔍 Search incidents by:

  * Type
  * Year or Month
  * Date range


## 🧪 **Data Display Output**

Data is shown in **tabular format** using the `tabulate` library:


+----+---------------+------------+-----------+------------+--------------------+
| ID | Incident Type | Date       | Latitude  | Longitude  | Description        |
+----+---------------+------------+-----------+------------+--------------------+
| 1  | Robbery       | 2025-07-01 | 19.0760   | 72.8777    | ATM Robbery        |
+----+---------------+------------+-----------+------------+--------------------+

## ⚙️ **Tech Stack**

| Component             | Description                                               |
| --------------------- | --------------------------------------------------------- |
| **Python 3.x**        | Core development language                                 |
| **MySQL**             | Backend relational database                               |
| **Geopy / Geocoding** | Converts user-entered locations into lat/long coordinates |
| **tabulate**          | CLI table formatting for neat data display                |
| **Modular Python**    | Layered structure (DAO, Entity, Exception, Utility, etc.) |


## ▶️ **How to Run**

### 🔌 **Prerequisites**

* Python 3.x
* MySQL server with `cars` schema created
* Internet connection (required for geolocation)

### 🛠️ **Installation**

Install required libraries:
pip install mysql-connector-python geopy tabulate

### 🚀 **Run the Application**
cd main
python main_module.py

## 🧭 **Sample Workflow**

1. ✅ Add victim, suspect, and law enforcement agency
2. 📍 Add a new **incident** using just the **location name**
3. 🧾 Add evidence and assign officers
4. 🗂️ Create a case and associate incidents
5. 📊 Generate reports based on:

   * Today
   * Month/Year
   * Custom range

## ❗ **Validations & Error Handling**

* ❌ Empty fields are flagged immediately
* 📅 Dates must be in `YYYY-MM-DD` format
* 📧 Email validation:

  * `@gmail.com` for victims, suspects, officers
  * `@police.gov` for law enforcement agencies
* 🌐 Invalid location → shown clearly with error
* 🧨 Custom exception `IncidentNumberNotFoundException` is handled



## 📈 **Use Case Scenarios**

| 👤 Role           | 🎯 Purpose                                       |
| ----------------- | ------------------------------------------------ |
| Crime Analyst     | Study crime patterns, frequency, and location    |
| Police Department | Record cases, assign officers                    |
| Investigators     | Track suspects, victims, incidents, and evidence |
| Admin Staff       | Generate daily/monthly/yearly crime reports      |


## 💡 **Future Enhancements**

* 🌐 Web Interface using Flask/Django
* 🔐 Role-based login (Admin, Officer)
* 📊 Heatmaps and crime data visualization (folium, matplotlib)
* 📤 Export reports to PDF/CSV
* 📱 SMS/email alerts for new incidents or report summaries


> ✅ *This project is a complete CLI-based simulation of a real-world Crime Reporting and Analysis System built using modular Python and MySQL backend. Perfect for case study implementations, prototypes, or extensions into full-stack applications.*

---

Let me know if you'd like this exported as a **PDF** or want a **Word doc version** for presentation purposes.
