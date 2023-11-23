#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my first module.

options:
    content:
        description: Data for put on created file.
        required: true
        type: str
    path:
        description: Path for create dile
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@ivannikita)
'''

EXAMPLES = r'''
# Pass in a message
- name: Create file with content
  my_namespace.my_collection.my_test:
    path: "/tmp"
    content: "Content of file"


'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: 
    type: str
    returned: always
    sample: ''
message:
    description: 
    type: str
    returned: always
    sample: ''
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():

    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=True,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    import os 
    
    if os.path.isfile(module.params['path']):
         result['changed'] = False
     
    
    
    with open(module.params['path'], 'w') as f:
      f.write(module.params['content'])
    if module.check_mode:
        module.exit_json(**result)
    result['original_message'] = module.params['path']
    result['message'] = 'Create file {}'.format(module.params['path'])
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()