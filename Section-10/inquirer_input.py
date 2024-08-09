import inquirer
confirm = {
    inquirer.Confirm('confirmed',
                    message="Do you want to enter the door ?" ,
                    default=True),
}
confirmation = inquirer.prompt(confirm)
print (confirmation["confirmed"])

questions = [
    inquirer.List('size',
                message="What size do you need?",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            ),
]
answers = inquirer.prompt(questions)
print (answers["size"])