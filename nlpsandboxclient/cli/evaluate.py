#!/usr/bin/env python3
import json

import click
from nlpsandboxclient import client, evaluation, utils


@click.group(name='evaluate', no_args_is_help=True)
def cli():
    """Evaluation related commands"""


@cli.command(name="prediction", no_args_is_help=True)
@click.option('--pred_filepath', help='Prediction filepath',
              type=click.Path(exists=True), required=True)
@click.option('--gold_filepath', help='Gold standard filepath',
              type=click.Path(exists=True), required=True)
@click.option('--output', help='Specify output json path',
              type=click.Path())
@click.option('--eval_type', help='Type of evaluation.',
              type=click.Choice(['date', 'person', 'address'],
                                case_sensitive=False))
def evaluate_prediction(pred_filepath, gold_filepath, output, eval_type):
    """Evaluate the performance of a local prediction file"""
    eval_mapping = {
        "date": evaluation.DateEvaluation,
        "person": evaluation.PersonNameEvaluation,
        "address": evaluation.PhysicalAddressEvaluation
    }
    evaluator = eval_mapping[eval_type]()

    evaluator.convert_dict(pred_filepath, gold_filepath)
    results = evaluator.eval()
    utils.stdout_or_json(results, output)


@cli.command(no_args_is_help=True)
@click.option('--annotator_host', help='Annotator host.')
@click.option('--note_json', help='Clinical notes json',
              type=click.Path(exists=True))
@click.option('--output', help='Specify output json path',
              type=click.Path())
@click.option('--annotator_type', help='Type of annotator.',
              type=click.Choice(['date', 'person', 'address'],
                                case_sensitive=False))
def annotate_note(annotator_host, note_json, output, annotator_type):
    """Annotate a note with specified annotator

    >>> nlp-cli evaluate annotate-note \
        --annotator_host http://10.23.55.45:9000/api/v1 \
        --note_json notes.json \
        --annotator_type date
    """
    with open(note_json, "r") as note_f:
        notes = json.load(note_f)
    all_annotations = []
    for note in notes:
        note.pop("id")
        annotations = client.annotate_note(host=annotator_host,
                                           note={"note": note},
                                           annotator_type=annotator_type)
        annotations['annotationSource'] = {
            "resourceSource": {
                "name": note['note_name']
            }
        }
        all_annotations.append(annotations)
    utils.stdout_or_json(all_annotations, output)


@cli.command(no_args_is_help=True)
@click.option('--annotator_host', help='Annotator host')
@click.option('--output', help='Specify output json path',
              type=click.Path())
def get_annotator(annotator_host, output):
    """Get annotator tool endpoint"""
    tool = client.get_annotator(
        host=annotator_host
    )
    utils.stdout_or_json(tool.to_dict(), output)


if __name__ == '__main__':
    cli()
