from __future__ import annotations

import sys
from pathlib import Path

from bhume import load, score, write_predictions
from bhume.baseline import global_median_shift


def make_predictions(village_dir: str):
    village = load(village_dir)

    preds = global_median_shift(village, confidence=0.55)
    plots = village.plots

    recorded_total_sqm = (
        plots["recorded_area_sqm"].fillna(0)
        + plots["pot_kharaba_ha"].fillna(0) * 10000
    )

    area_ratio = plots["map_area_sqm"] / recorded_total_sqm

    suspicious_area = (
        (recorded_total_sqm <= 0)
        | (area_ratio < 0.65)
        | (area_ratio > 1.55)
    )

    preds["method_note"] = (
        "corrected with median village-wide shift; area check used for restraint"
    )

    preds.loc[suspicious_area, "status"] = "flagged"
    preds.loc[suspicious_area, "geometry"] = plots.loc[suspicious_area, "geometry"]
    preds.loc[suspicious_area, "confidence"] = 0.0
    preds.loc[suspicious_area, "method_note"] = (
        "flagged: drawn area differs strongly from recorded total area"
    )

    return village, preds


def main(village_dir: str) -> None:
    village, preds = make_predictions(village_dir)

    output_path = Path(village_dir) / "predictions.geojson"
    write_predictions(output_path, preds)

    print(f"wrote predictions to {output_path}")

    if village.example_truths is not None:
        print(score(preds, village))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/vadnerbhairav")