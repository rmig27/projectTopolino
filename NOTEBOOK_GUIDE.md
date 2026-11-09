# Topolino learning notebooks

A guided path through the concepts represented in the project notebooks. Each topic has two versions:

- `NN_topic.ipynb` starts with imports and uses package functions, explaining them where they enter the experiment.
- `NN_topic_full.ipynb` develops the same workflow with function definitions introduced in context.

The sequence consolidates repeated draft and paper notebooks into separate teaching examples. Existing paper notebooks and their final plots stay in `paper/` and are not replaced by these tutorials. Where a concept appeared in both, the paper notebook was the primary reference. Where a paper figure exists, the lesson includes its original plotting code cell and saved output unchanged. If there is no paper counterpart, a matching draft cell is used when available. Topics without a matching source figure remain plotless. Hardware-specific acquisition is treated as a measurement workflow; the examples do not move equipment.

## Sequence

1. `01_gaussian.ipynb` — Gaussian field and RMS width (the first matched pair)
2. Fourier transforms — sampled signals and spatial frequency
3. Free-space propagation — Fresnel propagation and Gaussian diffraction
4. Thin lenses — phase curvature and focus
5. Diffraction gratings — orders and angle
6. Slits — single-slit diffraction and double-slit interference
7. Spiral beams — vortex phase
8. Tilt and phase masks — phase ramps
9. Zone plates — focusing and through-focus response
10. Holograms — interference and reconstruction
11. Speckle — random phase and propagation
12. Gerchberg–Saxton — phase retrieval from two planes
13. Camera calibration — ADU to power density
14. Through-focus measurements — image stacks and stage calibration
15. Grating experiment — source-to-detector simulation

16. `camera_and_stage_acquisition` — camera/stage acquisition workflow
17. `data_collection_and_metadata` — image stacks, reductions, and saved metadata
