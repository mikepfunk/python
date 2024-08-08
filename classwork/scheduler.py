'''Scheduler that schedules meetings and stores them in a JSON file.
'''
import json
from datetime import datetime


class MeetingScheduler:
    '''Class MeetingScheduler: Class to manage meeting scheduling and storage.'''
    def __init__(self, filepath):
        """
        Initializes the MeetingScheduler with a specified JSON file path.
        Args:
            filepath (str): The path to the JSON file for storing meeting data.
        """
        self.filepath = filepath  # Store the filepath for later use in saving and loading meetings.
        self.meetings = []  # Initialize an empty list to store meeting details.
        self.load_meetings()  # Load meetings from the JSON file if it exists.

    def schedule_meeting(self, name, participant, date, time):
        """
        Schedules a new meeting and saves it to the JSON file.
        Args:
            name (str): The name of the meeting.
            participant (str): The name of the participant scheduling the meeting.
            date (str): The date of the meeting in YYYY-MM-DD format.
            time (str): The time of the meeting in HH:MM format.
        """
        # Create a dictionary for the meeting details.
        meeting = {
            'id': len(self.meetings) + 1,  # Automatically assign an ID.
            'name': name,
            'participant': participant,
            'date': date,
            'time': time
        }
        self.meetings.append(meeting)  # Add the meeting to the list of meetings.
        self.save_meetings()  # Save the updated list of meetings to the JSON file.

    def display_weekly_meetings(self):
        """
        Displays all meetings scheduled for the current week.
        """
        print("Meetings scheduled for this week:")
        current_week = datetime.now().isocalendar()[1]  # Get the current week number.
        for meeting in self.meetings:
            meeting_date = datetime.strptime(meeting['date'], "%Y-%m-%d")
            if meeting_date.isocalendar()[1] == current_week:  # Check if the meeting is in the current week.
                print(f"{meeting['id']}: {meeting['name']} by {meeting['participant']} on {meeting['date']} at {meeting['time']}")

    def delete_meeting(self, meeting_id):
        """
        Deletes a specific meeting by ID.
        Args:
            meeting_id (int): The ID of the meeting to delete.
        """
        self.meetings = [meeting for meeting in self.meetings if meeting['id'] != meeting_id]  # Remove the meeting from the list.
        self.save_meetings()  # Save the updated list to the JSON file.

    def save_meetings(self):
        """
        Saves all meetings to the specified JSON file.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:  # Open the file in write mode.
            json.dump(self.meetings, file, indent=4)  # Write the list of meetings to the file with indentation for readability.

    def load_meetings(self):
        """
        Loads meetings from the specified JSON file.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:  # Open the file in read mode.
                self.meetings = json.load(file)  # Load the list of meetings from the file.
        except FileNotFoundError:
            self.meetings = []  # If the file does not exist, start with an empty list.

def get_input(prompt):
    """
    Gets user input based on a prompt.
    Args:
        prompt (str): The prompt displayed to the user.
    Returns:
        str: The user's input.
    """
    return input(prompt)

def main():
    """
    Main function to run the Meeting Scheduler application.
    """
    filepath = get_input("Enter the path to the JSON file for storing meeting data: ")  # Ask user for the file path.
    scheduler = MeetingScheduler(filepath)  # Create a MeetingScheduler instance with the specified file path.
    while True:
        # Display the menu options.
        print("\nMeeting Scheduler Menu:")
        print("1. Schedule a new meeting")
        print("2. Show this week's meetings")
        print("3. Delete a meeting")
        print("4. Exit")
        choice = get_input("Choose an option: ")  # Get the user's choice.

        if choice == '1':
            name = get_input("Enter the meeting name: ")
            participant = get_input("Enter your name: ")
            date = get_input("Enter the date of the meeting (YYYY-MM-DD): ")
            time = get_input("Enter the time of the meeting (HH:MM): ")
            scheduler.schedule_meeting(name, participant, date, time)
            print("Meeting scheduled successfully.")
        elif choice == '2':
            scheduler.display_weekly_meetings()
        elif choice == '3':
            meeting_id = int(get_input("Enter the meeting ID to delete: "))
            scheduler.delete_meeting(meeting_id)
            print("Meeting deleted successfully.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
