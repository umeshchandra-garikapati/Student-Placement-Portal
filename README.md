# SAHE Placement & No-Dues Portal — Firebase Google Sign-In

This project adds a Google authentication screen to the SAHE Placement & No-Dues Portal prototype.

## What it does
- Shows Google sign-in before the dashboard.
- Treats `syamcharan43@gmail.com` as the administrator.
- Treats other authenticated Google accounts as read-only visitors.
- Hides fee management, fee amounts, admin action buttons, reports/exports, and settings from visitors in the interface.
- Preserves the existing sample dashboard and local campus video.

## Step 1 — Create a Firebase project
1. Open https://console.firebase.google.com/ and sign in with a Google account.
2. Click **Create a project** and name it `SAHE Placement Portal` (or another name).
3. Complete the setup wizard. Analytics is optional for this prototype.

## Step 2 — Enable Google sign-in
1. In Firebase Console, open **Build → Authentication**.
2. Click **Get started** if prompted.
3. Open **Sign-in method** (or **Sign-in providers**), choose **Google**, enable it, select a support email, and save.

## Step 3 — Register a Web App and copy its config
1. Open Project Overview and click the web icon `</>` to add a Web App.
2. Name it `SAHE Portal Web`. Firebase Hosting is optional; you do not need to set it up to test locally.
3. Register the app and copy the Firebase web config values.
4. Open this project's `config.js` and replace the placeholder values:
   - `apiKey` with Firebase's `apiKey`
   - `authDomain` with Firebase's `authDomain`
   - `projectId` with Firebase's `projectId`
   - `appId` with Firebase's `appId`
5. Keep `adminEmail` as `syamcharan43@gmail.com` if that is the account that should be admin. Save with Ctrl+S.

Example format only (not real credentials):
```js
window.SAHE_AUTH_CONFIG = {
  apiKey: 'AIza...your-value...',
  authDomain: 'your-project-id.firebaseapp.com',
  projectId: 'your-project-id',
  appId: '1:123456789:web:abcdef',
  adminEmail: 'syamcharan43@gmail.com'
};
```

Do not place service-account private keys in `config.js`. The Firebase web config is meant to be used by client applications; database security must still be configured separately.

## Step 4 — Allow local testing
1. In Firebase Console, open **Authentication → Settings → Authorized domains**.
2. Ensure `localhost` is listed. Add it if missing. Firebase usually includes it for local development.
3. Use the local address `http://localhost:8000` when testing. Do not use `file://` to open `index.html` directly.

## Step 5 — Run the portal on Windows
1. Extract the ZIP.
2. Open the extracted `sahe-portal` folder in VS Code.
3. Choose **Terminal → New Terminal**.
4. Run:
```powershell
py server.py
```
5. Open http://localhost:8000 in Chrome.
6. Click **Continue with Google** and choose your Google account.

If `py server.py` does not work, try `python -m http.server 8000` from the same folder.

## Step 6 — Test roles
- Sign in as `syamcharan43@gmail.com`: the UI should show administrator features.
- Sign out and sign in with another Google account: the UI should show the read-only visitor interface, without fee pages or admin action buttons.

## Important security limitation
This remains a **frontend prototype**. Sample records are stored in each browser's `localStorage`, so they do not sync across users or devices. The role checks and hidden UI are implemented in browser JavaScript and can be bypassed by a technically skilled user. Do not use real student personal information or actual fee balances until the data is moved to a database with server-side authorization/security rules. Firebase Authentication verifies identity; it does not by itself protect localStorage data.

## Included features
- 30 fictional sample student records.
- Student profile form, photo upload/camera capture, placement tracking, no-dues checklist, analytics, CSV import/export and curated college FAQ chatbot.
- Campus video at `assets/campus-video.mp4`.
- QR-code and UPI payment options are not included.
