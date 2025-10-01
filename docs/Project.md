Of course. Here is a formalized and organized project overview, a detailed feature breakdown, and a complete set of test requirements based on your provided Markdown file.

---

### **Project Overview: Modern Digital Library System for "ወጣት ማእከል ላይብረሪ"**

**1. Introduction**

This document outlines the comprehensive features and requirements for the **Modern Digital Library System**, a full-stack web application designed for the "ወጣት ማእከል ላይብረሪ" (Youth Center Library). The primary goal of this project is to provide students with seamless online access to a digital collection of resources in a modern, intuitive, and aesthetically pleasing interface.

The system will function as a centralized hub where administrators can manage a core library of system-wide documents, and users can curate their own personal collections. The application will be accessible via the internet, ensuring availability for all authenticated members.

This project is developed by **Ethco Coders**.

**2. Core Concept**

The user experience is centered around a three-panel dashboard that provides a clear and organized workspace. Users will interact with two main types of content:
*   **System Catalogue:** A read-only collection of folders and files managed exclusively by administrators, available to all users.
*   **My Books (Custom Folders):** A private, user-managed space where individuals can create their own folder structures and upload their personal PDF files.

All PDF documents, whether from the system catalogue or a user's personal collection, will be opened in a clean, integrated, built-in PDF viewer, creating a consistent and uninterrupted reading experience.

**3. Design Philosophy**

The user interface will be a key differentiator. The design will move away from traditional file-system aesthetics and adopt a look and feel that resembles a modern digital book catalogue. This will be achieved through:
*   **Modern & Aesthetic UI:** A professional and clean design using a consistent color palette, typography, and iconography.
*   **Catalogue-Style Layout:** Folders and files will be represented by larger, decoratively styled cards or tiles rather than small, standard system icons, enhancing the "library" feel.
*   **Intuitive Navigation:** A clear separation of concerns between recent activity, main content browsing, and account management.

**4. File Management**

when user experience the main bar where all books list they will get a list of books, system files and custom files. 
*   **System Folder:** location Source/System/*
*   **Custom Folder:** location Source/Custom/*
*   **Folders:** any folder listed under either folders will belongs to correspond folder.  


---

### **Detailed Feature Breakdown**

#### **1. Public-Facing & Authentication System**

*   **1.1. Landing Page:**
    *   Serves as the initial entry point for all visitors.
    *   Presents a concise overview of the library system's features and benefits.
    *   Contains clear "Login" and "Sign Up" call-to-action buttons that redirect to the authentication page.
*   **1.2. Authentication Page:**
    *   A dedicated page for user registration (Sign Up) and login (Login).
    *   Upon successful authentication, users are automatically redirected to their personal dashboard.

#### **2. Main User Dashboard (3-Panel Layout)**

*   **2.1. Panel 1: Recent Activity Bar**
    *   A dedicated sidebar or top bar that displays a list of the most recently opened or accessed PDF files.
    *   Provides quick, one-click access to resume reading.

*   **2.2. Panel 2: Main Application / Library Bar**
    *   **2.2.1. Content Display:**
        *   Lists all available folders, clearly distinguishing between "System Folders" and the user's custom "My Books" section.
        *   Clicking a folder displays its contents (sub-folders and files).
    *   **2.2.2. System Folders (Admin-Managed):**
        *   Visible to all authenticated users.
        *   Users can navigate and open files within these folders.
        *   Users have read-only permissions: they cannot create, rename, or delete system-level folders or files. Management options (e.g., "3-dots menu") will be absent for these items.
    *   **2.2.3. Custom Folders (User-Managed):**
        *   **Folder Creation:** A "Create Folder" icon allows users to create new top-level folders in their personal space. Users will be prompted to enter a name.
        *   **Sub-folder Creation:** Inside a custom folder, an icon allows the creation of nested sub-folders.
        *   **File Upload:** Inside a custom folder, an icon allows users to upload a PDF file. The user provides a display name for the file, and the `.pdf` extension will be hidden in the UI to maintain the catalogue look.
        *   **Item Management:** Each user-created folder and file will feature a "3-dots" menu icon providing "Rename" and "Delete" options.
    *   **2.2.4. Integrated PDF Viewer:**
        *   A built-in application component.
        *   Clicking on any PDF file from any location (System or Custom) will open it directly within this viewer, preventing the need to leave the application or download files.
        *   The viewer should be seamlessly integrated into the main application layout.
    *   **2.2.5. User Experience Enhancements:**
        *   A "Sort By" feature to organize files and folders (e.g., by name, date modified).
        *   The footer or another visible, non-intrusive area will contain the text: **"Powered by Ethco Coders"**.

*   **2.3. Panel 3: User Account Bar**
    *   Displays the user's profile information.
    *   **Profile Picture:** Shows the user's current picture or a default contact icon. Allows users to upload/change their profile photo.
    *   **User Name:** Displays the user's full name.
    *   **Account Management:**
        *   Change Password functionality.
        *   Theme Toggle: An option to switch between a Bright (Light) and Dark mode for the application UI.
        *   Logout button.

#### **3. Admin Panel**

*   A separate, secure interface accessible only to users with administrator privileges.
*   **3.1. System Content Management:**
    *   Full CRUD (Create, Read, Update, Delete) capabilities for the system-wide folders and files that are visible to all users.
    *   Uploaded files and created folders will be stored server-side and immediately available to the entire user base.
*   **3.2. User Management:**
    *   A dedicated page to view a list of all registered users in the system.
    *   Ability to view details about a user, including the custom folders and files they have created.

---

### **Test Requirements & Development Checklist**

Here are the features relisted as a todo-style checklist for tracking development progress and quality assurance testing.

#### **Authentication & Onboarding**
- [ ] **Landing Page:**
    - [ ] Landing page loads successfully for unauthenticated users.
    - [ ] Page content accurately describes the library system.
    - [ ] "Login" button is visible and redirects to the authentication page.
    - [ ] "Sign Up" button is visible and redirects to the authentication page.
- [ ] **Authentication:**
    - [ ] User can successfully create a new account (Sign Up).
    - [ ] User can successfully log in with existing credentials.
    - [ ] User receives an error message for incorrect login credentials.
    - [ ] Successful login redirects the user to the main dashboard.

#### **Main Dashboard & UI**
- [ ] **General Layout:**
    - [ ] The 3-panel layout (Recent, Main, Account) is correctly displayed after login.
    - [ ] The UI is modern, professional, and uses a consistent design palette.
    - [ ] The "Powered by Ethco Coders" text is visible in its designated place.
- [ ] **Panel 1: Recent Activity Bar:**
    - [ ] The "Recent" bar is visible.
    - [ ] Opening a file adds it to the top of the "Recent" list.
    - [ ] Clicking an item in the "Recent" list opens the corresponding file in the PDF viewer.
- [ ] **Panel 2: Main Application Bar:**
    - [ ] **System Content:**
        - [ ] System-managed folders are visible to the user.
        - [ ] User can click and view the contents of system folders.
        - [ ] User can click and open system files in the PDF viewer.
        - [ ] The "3-dots" management menu is NOT visible on system folders or files.
        - [ ] User cannot drag, rename, delete, or add files to system folders.
    - [ ] **User's Custom Content ("My Books"):**
        - [ ] User can create a new top-level custom folder.
        - [ ] User can create a new sub-folder inside a custom folder.
        - [ ] User can upload a PDF file into a custom folder.
        - [ ] Uploaded file displays the user-provided name, without the `.pdf` extension.
        - [ ] A "3-dots" menu is visible on all user-created folders and files.
        - [ ] User can successfully rename a custom folder via the menu.
        - [ ] User can successfully rename a custom file via the menu.
        - [ ] User can successfully delete a custom folder via the menu (with confirmation).
        - [ ] User can successfully delete a custom file via the menu (with confirmation).
    - [ ] **Visuals & UX:**
        - [ ] Folder/file icons are styled as larger, catalogue-like items, not default system icons.
        - [ ] A "Sort By" control is present and functional.
- [ ] **Integrated PDF Viewer:**
    - [ ] Clicking any PDF file (System or Custom) opens the built-in viewer.
    - [ ] The PDF viewer correctly renders the content of the selected file.
    - [ ] The viewer is integrated within the app layout, not a new browser tab.
- [ ] **Panel 3: Account Bar:**
    - [ ] User's name and profile picture (or default icon) are displayed.
    - [ ] User can successfully upload a new profile picture.
    - [ ] "Change Password" functionality works as expected.
    - [ ] A theme toggle (Light/Dark mode) is present.
    - [ ] Toggling the theme correctly changes the application's appearance.
    - [ ] "Logout" button successfully ends the user session and redirects to the landing/login page.

#### **Admin Panel**
- [ ] **Access Control:**
    - [ ] Only users with admin privileges can access the admin panel.
    - [ ] Regular users are blocked from accessing admin routes.
- [ ] **System Content Management:**
    - [ ] Admin can create a new system-level folder.
    - [ ] Admin can rename an existing system folder.
    - [ ] Admin can delete a system folder.
    - [ ] Admin can upload a PDF file to a system folder.
    - [ ] Changes made by the admin are immediately reflected for all regular users.
- [ ] **User Management:**
    - [ ] Admin can view a complete list of all registered users.
    - [ ] Admin can select a user to view their created custom folders and files.
