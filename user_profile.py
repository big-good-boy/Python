# import user_profile_function

# user_profile = user_profile_function.build_profile('albert', 'einstein',
#                                                    location='princetin',
#                                                    field='physics')

# print(user_profile)


# from user_profile_function import build_profile

# user_profile = build_profile('albert', 'einstein',
#                              location='princetin',
#                              field='physics')

# print(user_profile)


# from user_profile_function import build_profile as profile

# user_profile = profile('albert', 'einstein',
#                        location='princetin',
#                        field='physics')

# print(user_profile)


import user_profile_function as profile

user_profile = profile.build_profile('albert', 'einstein',
                                     location='princetin',
                                     field='physics')

print(user_profile)