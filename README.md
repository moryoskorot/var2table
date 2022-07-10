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
 | ami | AMI to be used for the instance | `string` | ami-0d71ea30XXXXXXXX | no |
 | instance_type | Instance type to be used for the proxy. | `string` | t3.medium | no |
 | tags | A Map containing the tags for the various resources | `map("any")` | {'Created by': 'Terraform'} | no |

```

Which in a readme translates to 
 | Name | Description | Type | Default | Required |
 | --- | --- | --- | --- | :-: |
 | instance_name | Name for the instance | `string` | Radius Proxy | no |
 | subnet_id | Subnet id for the creation of the instance | `string` | n/a | yes |
 | ami | AMI to be used for the instance | `string` | ami-0d71ea30XXXXXXXX | no |
 | instance_type | Instance type to be used for the proxy. | `string` | t3.medium | no |
 | tags | A Map containing the tags for the various resources | `map("any")` | {'Created by': 'Terraform'} | no |
