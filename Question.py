from QuestionModels import MC_model

import click


@click.command()
@click.option("--model", prompt="Question Model ", help="Mutliple Choice Question")
@click.option("--count", default=1, help="Number of Questions")
def Question(count, model):
    """program a question MODEL for a total of COUNT times."""
    for _ in range(count):
        command = "MC_model.model_%s()" % model
        click.echo(f"Question {model}:")
        model = eval(command)
        model.generate(Print=True)


if __name__ == "__main__":
    Question()