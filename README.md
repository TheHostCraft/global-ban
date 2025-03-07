# Global Ban System 
de:
Hey, das ist der erste release eines Discord Bot von TheHostCraft Bot Labs (von TheHostCraft). Programmiert wurde dieser Bot von Jeremy Kirsch und hat die "Mozilla Public License 2.0" erhalten. Wir wollen euch erlauben den Bot Privat und Kommerziell zu nutzen, wollen aber auch Copyright/Credits für den bot erhalten. Daher die starke bitte, Lizenzgemäß das Copyright im Bot zu lassen! Unter folgendem Link ist einfach nachzulesen, was erlaubt ist und was nicht: https://choosealicense.com/licenses/mpl-2.0/

en:
Hey, this is the first released discord bot from TheHostCraft Bot Lab (from TheHostCraft). Coded got this bot from Jeremy Kirsch and got the "Mozilla Public License 2.0" license. We want to allow you to use this bot private and commercial but want to get some credits, so please don't remove the copyright from the bot. Here, you can easily understand what is under this license allowed: https://choosealicense.com/licenses/mpl-2.0/


# Features

- Global Ban
- Global Unban
- Slash Command
- App in Discord

## Requirements
- python 3.9 or higher
- ezcord
- python-dotenv
- pyYaml

## Bot Token Config

de:
Für den Bot Token nutzen wir dotenv um den Bot Token sicher in einer .env Datei zu speichern. Dazu einfach bei "YOUR_TOKEN_HERE" deinen Discord Bot Token eintragen!
en:
For the bot token we use dotenv, to save the bot token secured in a .env file. Just paste your bot token into "YOUR_TOKEN_HERE"!
```
DISCORD_TOKEN = YOUR_TOKEN_HERE
```
## Bot Config
de:
Wir haben eine glob-ban.yaml für die Konfiguration der Staff Rollen, des Main Servers und der Server, auf denen gebannt werden soll. Unter "required_roles" gibst du alle Rollen an, die Rechte haben sollen global zu bannen! Diese Rollen müssen auf dem Hauptserver sein, da dort abgefragt wird ob der Nutzer die Rollen hat. Bei "main_server_id" gibst du die ID deines Hauptservers an. Bei "global_ban_servers" gibst du alle Server an, auf denen gebannt werden soll. Wenn auf dem Hauptserver auch gebannt wird, musst du diesen auch angeben.
en:
We have a glob-ban.yaml for the configuration of the staff roles, the main server and the servers to be banned. Under “required_roles” you specify all roles that should have the right to ban globally! These roles must be on the main server, as this is where the system checks whether the user has the roles. For “main_server_id”, enter the ID of your main server. For “global_ban_servers”, enter all servers on which you want to ban the user. If the main server is also banned, you must also specify this.
```yaml
required_roles:  
 - 123456789
 - 1234567890
 - 1234567891
main_server_id: 123456789987
global_ban_servers:  
 - 1234567899876
 - 1234567899875 
 - 1234567899874
 - 1234567899873
 - 1234567899872
 - 1234567899871 
 - 1234567899870
 - 1234567899877
 - 1234567899878
```
## Report a problem / Support
de:
Wenn du irgendwelche Fehler hast oder Hilfe benötigst joine gerne unserem Discord oder öffne einen Issue auf Github.
en: 
If you have any bugs or need help, please join our Discord or open an issue on Github.
## Support Server:
de:
Du kannst dem offiziellen TheHostCraft Discord über diesen Link beitreten: https://discord.gg/DCDTNDK2eX
en:
You can join the official TheHostCraft discord over this link: https://discord.gg/DCDTNDK2eX
