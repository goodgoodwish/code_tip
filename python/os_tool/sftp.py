import pysftp

with pysftp.Connection(host="files.responsys.net",
                       username="blastwork_scp",
                       private_key="/Users/charliezhu/.ssh/rn_games_responsys_id_rsa",
                       ) as sftp:
    files = sftp.listdir()
    print(files)
    sftp.get("download/80022_BOUNCE_20180912_185817.txt.zip", "test.zip")

