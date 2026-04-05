import sys
import json
import prompt_toolkit
from prompt_toolkit import prompt


def show_menu():

    while True:
        user_response = input(">>> ")
        user_response = user_response.lower().strip()
        options = ["add", "delete", "edit", "exit", "list"]

        if user_response in options:
            return user_response
        else:
            print("Invalid input")


def add_reminder(reminders):
    text = input(">>> Enter reminder: ")

    reminder = {"text": text, "done": False}
    reminders.append(reminder)
    save_reminders(reminders)
    print("-----Added successfully-----")


def load_reminders():
    with open("reminders.json", "r") as file:
        reminder_list = json.load(file)

    return reminder_list


def save_reminders(reminders_to_save):
    with open("reminders.json", "w") as file:
        json.dump(reminders_to_save, file, indent=4)


def edit_reminder(reminders):
    edited = False
    while not edited:
        edit_index = input(">>> Enter index to be edited or use exit: ")
        if edit_index.lower().strip() == "exit":
            break

        elif (
            edit_index.isdigit()
            and int(edit_index) >= 0
            and int(edit_index) < len(reminders)
        ):
            target = int(edit_index)
            print("-----To quit use exit-----")
            print({reminders[target]["text"]})
            new_text = prompt(
                f"\n>>> Editing reminder #{edit_index}: ",
                default=reminders[target]["text"],
            )
            if new_text.lower().strip() == "exit":
                break

            reminders[target]["text"] = new_text
            print(f"-----Edit reminder #{edit_index}-----")
            save_reminders(reminders)
            edited = True

        else:
            print("Invalid input!")


def list_reminders(reminders):
    print("-----Your reminders-----")
    for index, reminder in enumerate(reminders):
        print(f"#{index}. Content: {reminder['text']} || Done: {reminder['done']}")


def delete_reminder(reminders):
    deleted = False
    while not deleted:
        delete_index = input(">>> Enter index to be deleted or use exit: ")
        if delete_index.lower().strip() == "exit":
            break

        elif (
            delete_index.isdigit()
            and int(delete_index) >= 0
            and int(delete_index) < len(reminders)
        ):
            while True:
                target = int(delete_index)
                confirmation = input(
                    f">>> Are you sure you want to delete the Reminder #{delete_index}: \"{reminders[target]['text']}\"? (yes/no): "
                )
                confirmation = confirmation.lower().strip()
                if confirmation == "yes":
                    removed_item = reminders.pop((target))
                    save_reminders(reminders)
                    print(f"-----Deleted reminder #{delete_index}-----")
                    deleted = True
                    break
                elif confirmation == "no":
                    break
                else:
                    print("Invalid input!")
        else:
            print("Invalid input!")


### MAIN ###


def main():
    print("\n-----Memory-----")
    print("Enter add/delete/edit/list")
    print("OR enter exit\n")
    reminders = load_reminders()

    while True:
        response = show_menu()

        if response == "exit":
            print("Goodbye!")
            sys.exit()

        elif response == "add":
            add_reminder(reminders)

        elif response == "list" or response == "delete" or response == "edit":
            list_reminders(reminders)

        if response == "delete":
            delete_reminder(reminders)

        if response == "edit":
            edit_reminder(reminders)


if __name__ == "__main__":
    main()
