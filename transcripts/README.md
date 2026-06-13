# AI Usage Transcript

## Tools Used
- Claude.ai (web) — problem understanding, debugging, solution design
- Claude Code (CLI) — implementation and code changes

## Claude.ai Conversation Link
https://claude.ai/share/137c8d41-96a2-4675-a9ed-d64d9167073f

## Claude Code Transcript
See `conversation-2026-06-13-221926.txt` in this folder.

## What I Used AI For
- Understanding the BhuMe challenge requirements
- Understanding the starter kit structure
- Debugging village folder loading issues
- Understanding GeoJSON outputs
- Running and interpreting baseline results
- Generating predictions.geojson files
- Adding per-plot confidence scoring based on area ratio deviation
- Setting up Git and GitHub repository
- Preparing submission structure

## My Approach
I started with the provided baseline solution.

The solution estimates a village-wide median shift using the provided example truth plots and applies that correction to all plots in the village.

Confidence was then made per-plot: deviation of area_ratio from 1.0 determines confidence (deviation < 0.1 → 0.85, < 0.2 → 0.75, < 0.35 → 0.65, else 0.55). Suspicious plots (area ratio outside 0.65–1.55) are flagged with confidence 0.

Predictions were generated for:
- Vadnerbhairav (IoU: 0.713, improvement: +0.112)
- Malatavadi (IoU: 0.588, improvement: +0.090)

## Future Improvements
- Using imagery.tif directly for visual boundary detection
- Using boundaries.tif signals
- Plot-specific corrections instead of a single village-wide shift
- Better confidence calibration

## Notes
AI tools were used for guidance, debugging, and understanding the codebase. Final repository setup, execution, testing, and submission preparation were performed manually.