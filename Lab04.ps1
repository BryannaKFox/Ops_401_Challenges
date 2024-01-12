# Script:                       ops401d10-Lab04
# Author:                       Bryanna Fox
# Date of latest revision:      1/11/2024
# Purpose:                      PowerShell script to configure security settings
 

# 1.1.5 (L1) Ensure 'Password must meet complexity requirements' is set to 'Enabled'
secedit /export /cfg C:\secpol.cfg
(Get-Content C:\secpol.cfg).replace("PasswordComplexity = 0", "PasswordComplexity = 1") | Set-Content C:\secpol.cfg
secedit /configure /db $env:windir\security\new.sdb /cfg C:\secpol.cfg /areas SECURITYPOLICY

# 18.4.3 (L1) Ensure 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)'
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "EnableInsecureGuestLogons" -Value 0

Write-Host "Configuration completed successfully."
