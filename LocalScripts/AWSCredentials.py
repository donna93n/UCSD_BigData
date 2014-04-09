### AWS credentials: ####
# Change entries here to match your own #
# Get values for the first two entries from the "Security crediential" Tab
# Under in the menu under your name.
aws_access_key_id='AKIAIXKAXYLKA6OZYK6A'
aws_secret_access_key='v0KFO/0dQVu0qKwThhL/AgKZhWUsZgoK8rH6pBIG'
# Get the Keypair in the EC2 Dashboard page.
keyPairFile="</c/Users/Donna\ Nguyen/.ssh/virginiaKeypair.pem>" # name of file keeping local key
key_name="virginiaKeypair" # name of keypair (not name of file where key is stored)
# Set the security group On the EC2 page (You will need to add IP addresses if
# you want to connect from a place previously unauthorized.
security_groups=['291']
### End of AWS credentials ####
