# 🌟 Guestbook 🌟

Welcome to the **Guestbook** project! This is a sleek, real-time guestbook application built using **FastHTML**, **HTMX**, and **Supabase**. Leave your mark and see messages from others instantly!

## 🚀 Overview

This project showcases a modern guestbook application with real-time updates and a clean, user-friendly interface. It's built with:
- **FastHTML**: A powerful Python framework for building HTML applications.
- **HTMX**: For seamless AJAX requests and dynamic updates.
- **Supabase**: A backend-as-a-service providing database storage and management.

- Demo Video
- 

https://github.com/user-attachments/assets/ea138446-0f7d-4446-82da-8fa5f48a8f43



## ✨ Features

- **Real-time updates**: See new messages as they are posted.
- **User-friendly interface**: Simple and intuitive design.
- **Easy setup**: Get up and running quickly with minimal configuration.

## 🛠️ Prerequisites

Before you begin, ensure you have the following:
- **Python 3.x** installed on your system.
- A **Supabase** account. Sign up if you haven't already.
- A **Supabase** project. Create a new project and note down your project URL and API key.

## 📦 Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/karanop001018/.git
    cd guestbook
    ```

2. **Install Dependencies**:
    ```bash
    pip install supabase-py python-dotenv pytz fasthtml
    ```

3. **Set Up Supabase**:
    - Create a new table named `guestbook` in your Supabase project with the following columns:
        - `id` (int8, primary key)
        - `name` (text)
        - `message` (text)
        - `timestamp` (text)
    - Create a `.env` file in the root directory of your project with the following content:
        ```env
        SUPABASE_URL=your_supabase_project_url
        SUPABASE_KEY=your_supabase_api_key
        ```
    - Replace `your_supabase_project_url` and `your_supabase_api_key` with your actual Supabase project URL and API key.

4. **Run the Application**:
    ```bash
    python main.py
    ```
    - Visit `http://localhost:5001` in your browser to see the guestbook in action.

## 🌍 Deployment

Deploy your guestbook application using your preferred hosting service.


## 🤝 Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For feedback, suggestions, or collaboration opportunities, reach out at mpkaranpatel01018@gmail.com.
