# Var2Table 
A small python script which takes a variables.tf file path and outputs it in a table format for a README.md file


Example usage :
``` 
var2table.py ~/terraform/project/modules/mymodule/variables.tf
```

The output will look like :
```
 | Name | Description | Type | Default | Required |
 | --- | --- | --- | --- | :-: |
 | instance_name | Name for the instance | `string` | Radius Proxy | no |
 | subnet_id | Subnet id for the creation of the instance | `string` | n/a | yes |
 | ami | AMI to be used for the instance | `string` | ami-0d71ea30463e0ff8d | no |
 | instance_type | Instance type to be used for the proxy. | `string` | t3.medium | no |
 | tags | A Map containing the tags for the various resources | `map("any")` | {'Created by': 'Terraform'} | no |
 | vpc_id | VPC Id , used for the SG | `string` | n/a | yes |
 | vpc_cidr | VPC CIDR , used for the SG | `string` | n/a | yes |
 | duo_port | Port to be used by duo (also whitelisted at the SG level) | `number` | 1812 | no |
 | user_data | StartupScript for the instance , should include the installation and configuration of the proxy. | `string` | n/a | yes |
 | integration_role_arn | AWS Role to be used for the process | `string` | n/a | yes |
 | directory_id | The AWS Directory ID | `string` | n/a | yes |
 | shared_secret | The shared secret used to authenticate between the radius proxy and the ad. | `string` | n/a | yes |
 | region | The region the AD is in. | `string` | n/a | yes |
 | integration_delay | Amount of delay before attempting to run the command. | `string` | 450s | no |
```

Which in a readme translates to 
 | Name | Description | Type | Default | Required |
 | --- | --- | --- | --- | :-: |
 | instance_name | Name for the instance | `string` | Radius Proxy | no |
 | subnet_id | Subnet id for the creation of the instance | `string` | n/a | yes |
 | ami | AMI to be used for the instance | `string` | ami-0d71ea30463e0ff8d | no |
 | instance_type | Instance type to be used for the proxy. | `string` | t3.medium | no |
 | tags | A Map containing the tags for the various resources | `map("any")` | {'Created by': 'Terraform'} | no |
 | vpc_id | VPC Id , used for the SG | `string` | n/a | yes |
 | vpc_cidr | VPC CIDR , used for the SG | `string` | n/a | yes |
 | duo_port | Port to be used by duo (also whitelisted at the SG level) | `number` | 1812 | no |
 | user_data | StartupScript for the instance , should include the installation and configuration of the proxy. | `string` | n/a | yes |
 | integration_role_arn | AWS Role to be used for the process | `string` | n/a | yes |
 | directory_id | The AWS Directory ID | `string` | n/a | yes |
 | shared_secret | The shared secret used to authenticate between the radius proxy and the ad. | `string` | n/a | yes |
 | region | The region the AD is in. | `string` | n/a | yes |
 | integration_delay | Amount of delay before attempting to run the command. | `string` | 450s | no |
