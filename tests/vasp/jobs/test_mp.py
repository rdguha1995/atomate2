import pytest
from pymatgen.core import Structure

from atomate2.vasp.flows.mp import MPMetaGGARelaxMaker, MPMetaGGAStaticMaker
from atomate2.vasp.sets.mp import MPMetaGGARelaxSetGenerator


def test_mp_meta_gga_static_maker(mock_vasp, clean_dir, vasp_test_dir):
    from emmet.core.tasks import TaskDoc
    from jobflow import run_locally

    # map from job name to directory containing reference output files
    ref_paths = {
        "MP meta-GGA static": "Si_mp_metagga_relax/r2scan_final_static",
    }
    si_struct = Structure.from_file(
        f"{vasp_test_dir}/Si_mp_metagga_relax/r2scan_final_static/inputs/POSCAR"
    )

    # settings passed to fake_run_vasp; adjust these to check for certain INCAR settings
    fake_run_vasp_kwargs = {
        key: {"incar_settings": ["LWAVE", "LCHARG"]} for key in ref_paths
    }

    mock_vasp(ref_paths, fake_run_vasp_kwargs)

    # generate flow
    job = MPMetaGGAStaticMaker(
        input_set_generator=MPMetaGGARelaxSetGenerator(auto_kspacing=0.8249)
    ).make(si_struct)

    # ensure flow runs successfully
    responses = run_locally(job, create_folders=True, ensure_success=True)

    # validate output
    output = responses[job.uuid][1].output
    assert isinstance(output, TaskDoc)
    assert output.output.energy == pytest.approx(-46.8613738)


def test_mp_meta_gga_relax_maker(mock_vasp, clean_dir, vasp_test_dir):
    from emmet.core.tasks import TaskDoc
    from jobflow import run_locally

    # map from job name to directory containing reference output files
    ref_paths = {
        "MP meta-GGA relax": "Si_mp_metagga_relax/r2scan_relax",
    }
    si_struct = Structure.from_file(
        f"{vasp_test_dir}/Si_mp_metagga_relax/r2scan_final_static/inputs/POSCAR"
    )

    # settings passed to fake_run_vasp; adjust these to check for certain INCAR settings
    fake_run_vasp_kwargs = {
        key: {"incar_settings": ["LWAVE", "LCHARG"]} for key in ref_paths
    }

    mock_vasp(ref_paths, fake_run_vasp_kwargs)

    # generate flow
    job = MPMetaGGARelaxMaker(
        input_set_generator=MPMetaGGARelaxSetGenerator(auto_kspacing=0.4786)
    ).make(si_struct)

    # ensure flow runs successfully
    responses = run_locally(job, create_folders=True, ensure_success=True)

    # validate output
    output = responses[job.uuid][1].output
    assert isinstance(output, TaskDoc)
    assert output.output.energy == pytest.approx(-46.86703814)
