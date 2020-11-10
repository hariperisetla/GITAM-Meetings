from dhooks import Webhook, Embed

import csv

def bot(hookName, username):
    if hookName == "":
        pass
    else:
        hook = Webhook(hookName)

        embed = Embed(
            description="GITAM Meetings",
            color=0xB1040E,
            timestamp="now"
        )

        embed.set_author(name="Meetings")
        with open('meet.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # print(row)
                title=row[0]
                dateandlink=row[1] + ", " + row[2]
                embed.add_field(name=title, value=dateandlink)
        
        footer = 'By ' + username

        embed.set_footer(text=footer)
        hook.send(embed=embed)