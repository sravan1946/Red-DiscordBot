from redbot.core.commands import Context, permissions_check
from redbot.core.utils.mod import is_mod_or_superior, check_permissions


def check_self_permissions():
    async def predicate(ctx: Context):
        return (
            bool(
                await check_permissions(ctx, {"manage_messages": True})
                or await is_mod_or_superior(ctx.bot, ctx.author)
            )
            if ctx.guild
            else True
        )

    return permissions_check(predicate)
