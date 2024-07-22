$newServerName = "NET2Grid-Server"

#Create OUs
Import-Module activedirectory

$ADOU = Import-csv "C:\Users\Administrator\Desktop\OUsNET2Grid.csv"

foreach ($ou in $ADOU)
{
#Map CSV coumn to variable
$name = $ou.name
$path = $ou.path

# Below command will create OU as per CSV
New-ADOrganizationalUnit `
-Name $name `
-path $path `

}

# Create users based on CSV file
$usersCSV = "C:\Users\Administrator\Desktop\EmployeeData.csv"
$users = Import-Csv $usersCSV

foreach ($user in $users) {
    $firstName = $user.Name
    $lastName = $user.Surname
    $title = $user.Title
    $department = $user.Department
    $initials = $user.Initials
    $username = "$firstName.$lastName"
    $password = ConvertTo-SecureString "Password123" -AsPlainText -Force
    $ouPath = $user.Path  # New column for OU path
    
    # Check if the username already exists
    if (-not (Get-ADUser -Filter {SamAccountName -eq $username})) {
        # Construct user properties
        $userParams = @{
            Name = $username  # Provide the Name parameter explicitly
            GivenName = $firstName
            Surname = $lastName
            Initials = $initials
            SamAccountName = $username
            UserPrincipalName = "$username@$domainName"
            DisplayName = "$firstName $lastName"
            Title = $title
            Department = $department
            AccountPassword = $password
            Enabled = $true
            Path = $ouPath  # Use specified OU path from the CSV
        }
        
        # Create the user
        New-ADUser @userParams
        Write-Host "User $username created in OU specified in the CSV."
    } else {
        Write-Host "User $username already exists. Skipping creation."
    }
}

#Renames the server
Rename-Computer -NewName $newServerName -Force 

Restart-Computer 
