from naas_drivers import linkedin
import naas
import pandas as pd

from LinkedinScripts.LinkedInConnect import LinkedinConnect

lkConn = LinkedinConnect()
lkConnectionObj = lkConn.connectToLinkedin()

# Schedule your notebook every hour
# naas.scheduler.add(cron="0 9 * * 1-5")

FIRST_MESSAGE = """Hello {},

Thank you for connecting with me on LinkedIn. I'm excited to be connected with professionals like you.

I noticed we share an interest in Tech Industry. I think it would be great to share insights and experiences with each other.

Additionally, I wanted to share my portfolio website with you: https://ameyportfolio.netlify.app

It showcases some of my recent projects and experiences in Data Engineering and Software Development as whole. I hope you find it interesting.

Looking forward to staying in touch!

Best regards,
Amey"""

df_invitation = lkConnectionObj.invitation.get_received()
print(f"Accepting {len(df_invitation)} pending Invites")

def accept_new_contact(df):
    df_accept = pd.DataFrame()

    # Loop
    for index, row in df.iterrows():
        fullname = row.FULLNAME
        status = row.INVITATION_STATUS
        invitation_id = row.INVITATION_ID
        shared_secret = row.SHARED_SECRET
        if status == "PENDING":
            print(fullname)
            tmp_df = lkConnectionObj.invitation.accept(invitation_id, shared_secret)
            df_accept = pd.concat([df_accept, tmp_df])
    return df_accept


df_accept = accept_new_contact(df_invitation)
print(df_accept)


def send_first_message(df):
    # Loop
    for index, row in df.iterrows():
        fullname = row.FULLNAME
        profile_id = row.PROFILE_ID
        print(fullname)
        lkConnectionObj.message.send(FIRST_MESSAGE.format(fullname), profile_id)


send_first_message(df_accept)
