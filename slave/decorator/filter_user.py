def filter_user(*users, reject_him=False):
    def decorator(func):
        async def wrapper(ctx, *args, **kwargs):
            match_found = False
            for user in users:
                if isinstance(user, int):
                    if ctx.author.id == user:
                        match_found = True
                        if reject_him:
                            return await ctx.send("You do not have permission to use this command.")
                elif isinstance(user, str):
                    if ctx.author.name == user:
                        match_found = True
                        if reject_him:
                            return await ctx.send("You do not have permission to use this command.")
            if not match_found and not reject_him:
                return await ctx.send("You do not have permission to use this command.")

            return await func(ctx, *args, **kwargs)

        return wrapper
    return decorator
