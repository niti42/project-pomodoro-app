# Pomodoro Timer Application

This is a simple **Pomodoro Timer** built using Python's Tkinter library. The Pomodoro technique is a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. This application automates the timing for work and break sessions.

## Key Features:

- **Work Sessions:** The timer is set for a 25-minute work session by default.
- **Short Breaks:** After each work session, a 5-minute break is triggered.
- **Long Breaks:** Every 4th work session (after 3 short breaks), a longer 20-minute break is triggered.
- **Reset Functionality:** The timer can be reset at any time, returning the session count to zero and clearing any checkmarks.
- **Visual Feedback:** The timer and session status (Work/Break) are displayed visually, along with a tick mark for each completed session.

## Code Breakdown:

### Constants:

- Color codes (`PINK`, `RED`, `GREEN`, `YELLOW`).
- Timer durations (`WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`).
- Global variables `reps` (to track the number of sessions) and `timer` (to manage the countdown).

### `reset_timer` Function:

- Resets the timer to 00:00.
- Resets the label to display "Timer".
- Clears any session checkmarks.
- Resets the session counter (`reps`).

### `start_timer` Function:

- Increments the session count (`reps`).
- Determines whether the current session is a work session, a short break, or a long break.
- Triggers the countdown mechanism with the appropriate time.

### `countdown` Function:

- Handles the countdown of seconds and updates the timer display.
- When the timer reaches zero, it automatically starts the next session (work or break).
- Displays tick marks for completed work sessions.

### UI Setup:

- Creates a window with a tomato image as the background.
- Displays the timer, start/reset buttons, and a label for session status.
- The application window's layout is managed using Tkinter's grid system.
