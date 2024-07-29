import config_utils


# load config from file path
config = config_utils.make(file_path="example.yaml")

print(config)

# add new attributes
config.help_policy.new_attr = 2134

print(config)
