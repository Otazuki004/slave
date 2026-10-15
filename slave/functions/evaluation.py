import sys
import io
import traceback
from discord.ext import commands
from discord import File, Embed
from discord.ext.commands.view import StringView
from slave import slave as Yuri
from slave.decorator.filter_user import filter_user


def p(code):
    print(code)


class EvalCommand(commands.Command):
    async def invoke(self, ctx):
        ctx.args = [ctx]
        ctx.kwargs = {}
        await self.callback(ctx)


@filter_user('gPunisher', 1515042523016593499)
async def evall(ctx):
    content = ctx.message.content
    parts = content.split(None, 1)

    if len(parts) < 2 or not parts[1].strip():
        return await ctx.send("Please enter code to run it!")

    code = parts[1]

    stats = await ctx.send("Loading...")

    replied_message = (
        ctx.message.reference.resolved
        if ctx.message.reference
        else None
    )

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = io.StringIO()
    redirected_error = io.StringIO()
    exc = None

    try:
        sys.stdout = redirected_output
        sys.stderr = redirected_error

        namespace = {
            **globals(),
            "ctx": ctx,
            "replied_message": replied_message,
        }

        exec(
            "async def __aexec(ctx, replied_message):\n"
            + "".join(f"    {line}\n" for line in code.splitlines()),
            namespace,
        )

        await namespace["__aexec"](ctx, replied_message)

    except Exception:
        exc = traceback.format_exc()

    finally:
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        redirected_output.close()
        redirected_error.close()

    evaluation = (
        exc
        if exc
        else stderr
        if stderr
        else stdout
        if stdout
        else "Success"
    )

    output_code = evaluation.strip()

    if len(output_code) > 3500:
        with io.BytesIO(evaluation.encode()) as out_file:
            out_file.name = "eval_output.txt"
            await ctx.send(
                "Output too big, sending as file:",
                file=File(out_file),
            )
    else:
        embed = Embed(
            title="Output",
            description=f"```python\n{output_code}\n```",
            color=0x1E90FF,
        )
        await ctx.send(embed=embed)

    await stats.delete()


async def setup(Yuri):
    Yuri.add_command(EvalCommand(evall, name="eval"))
