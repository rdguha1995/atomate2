"""
Module defining jobs for Materials Project r2SCAN workflows.

Reference: https://doi.org/10.1103/PhysRevMaterials.6.013801
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from atomate2.vasp.jobs.base import BaseVaspMaker
from atomate2.vasp.sets.mp import MPGGARelaxGenerator, MPMetaGGARelaxGenerator

if TYPE_CHECKING:
    from atomate2.vasp.sets.base import VaspInputGenerator

__all__ = ["MPPreRelaxMaker", "MPMetaGGARelaxMaker", "MPMetaGGAStaticMaker"]


@dataclass
class MPGGARelaxMaker(BaseVaspMaker):
    """
    Maker to create VASP relaxation job using PBE GGA by default.

    Parameters
    ----------
    name : str
        The job name.
    input_set_generator : .VaspInputGenerator
        A generator used to make the input set.
    write_input_set_kwargs : dict
        Keyword arguments that will get passed to :obj:`.write_vasp_input_set`.
    copy_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.copy_vasp_outputs`.
    run_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.run_vasp`.
    task_document_kwargs : dict
        Keyword arguments that will get passed to :obj:`.TaskDoc.from_directory`.
    stop_children_kwargs : dict
        Keyword arguments that will get passed to :obj:`.should_stop_children`.
    write_additional_data : dict
        Additional data to write to the current directory. Given as a dict of
        {filename: data}. Note that if using FireWorks, dictionary keys cannot contain
        the "." character which is typically used to denote file extensions. To avoid
        this, use the ":" character, which will automatically be converted to ".". E.g.
        ``{"my_file:txt": "contents of the file"}``.
    """

    name: str = "MP GGA Relax"
    input_set_generator: VaspInputGenerator = field(
        default_factory=lambda: MPGGARelaxGenerator(auto_ismear=False)
    )


@dataclass
class MPGGAStaticMaker(BaseVaspMaker):
    """
    Maker to create VASP static job using PBE GGA by default.

    Parameters
    ----------
    name : str
        The job name.
    input_set_generator : .VaspInputGenerator
        A generator used to make the input set.
    write_input_set_kwargs : dict
        Keyword arguments that will get passed to :obj:`.write_vasp_input_set`.
    copy_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.copy_vasp_outputs`.
    run_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.run_vasp`.
    task_document_kwargs : dict
        Keyword arguments that will get passed to :obj:`.TaskDoc.from_directory`.
    stop_children_kwargs : dict
        Keyword arguments that will get passed to :obj:`.should_stop_children`.
    write_additional_data : dict
        Additional data to write to the current directory. Given as a dict of
        {filename: data}. Note that if using FireWorks, dictionary keys cannot contain
        the "." character which is typically used to denote file extensions. To avoid
        this, use the ":" character, which will automatically be converted to ".". E.g.
        ``{"my_file:txt": "contents of the file"}``.
    """

    name: str = "MP GGA Static"
    input_set_generator: VaspInputGenerator = field(
        default_factory=lambda: MPGGARelaxGenerator(
            user_incar_settings={"NSW": 0, "ISMEAR": -5, "LREAL": False},
            auto_ismear=False,
        )
    )


@dataclass
class MPPreRelaxMaker(BaseVaspMaker):
    """
    Maker to create VASP pre-relaxation job using PBEsol by default.

    Parameters
    ----------
    name : str
        The job name.
    input_set_generator : .VaspInputGenerator
        A generator used to make the input set.
    write_input_set_kwargs : dict
        Keyword arguments that will get passed to :obj:`.write_vasp_input_set`.
    copy_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.copy_vasp_outputs`.
    run_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.run_vasp`.
    task_document_kwargs : dict
        Keyword arguments that will get passed to :obj:`.TaskDoc.from_directory`.
    stop_children_kwargs : dict
        Keyword arguments that will get passed to :obj:`.should_stop_children`.
    write_additional_data : dict
        Additional data to write to the current directory. Given as a dict of
        {filename: data}. Note that if using FireWorks, dictionary keys cannot contain
        the "." character which is typically used to denote file extensions. To avoid
        this, use the ":" character, which will automatically be converted to ".". E.g.
        ``{"my_file:txt": "contents of the file"}``.
    """

    name: str = "MP pre-relax"
    input_set_generator: VaspInputGenerator = field(
        default_factory=lambda: MPMetaGGARelaxGenerator(
            user_incar_settings={
                "EDIFFG": -0.05,
                "METAGGA": None,
                "GGA": "PS",
                "LWAVE": True,
                "LCHARG": True,
            },
            auto_ismear=False,
        )
    )


@dataclass
class MPMetaGGARelaxMaker(BaseVaspMaker):
    """
    Maker to create VASP relaxation job using r2SCAN by default.

    Parameters
    ----------
    name : str
        The job name.
    input_set_generator : .VaspInputGenerator
        A generator used to make the input set.
    write_input_set_kwargs : dict
        Keyword arguments that will get passed to :obj:`.write_vasp_input_set`.
    copy_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.copy_vasp_outputs`.
    run_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.run_vasp`.
    task_document_kwargs : dict
        Keyword arguments that will get passed to :obj:`.TaskDoc.from_directory`.
    stop_children_kwargs : dict
        Keyword arguments that will get passed to :obj:`.should_stop_children`.
    write_additional_data : dict
        Additional data to write to the current directory. Given as a dict of
        {filename: data}. Note that if using FireWorks, dictionary keys cannot contain
        the "." character which is typically used to denote file extensions. To avoid
        this, use the ":" character, which will automatically be converted to ".". E.g.
        ``{"my_file:txt": "contents of the file"}``.
    """

    name: str = "MP meta-GGA relax"
    input_set_generator: VaspInputGenerator = field(
        default_factory=lambda: MPMetaGGARelaxGenerator(
            user_incar_settings={"LWAVE": True, "LCHARG": True}, auto_ismear=False
        )
    )


@dataclass
class MPMetaGGAStaticMaker(BaseVaspMaker):
    """
    Maker to create VASP static job using r2SCAN by default.

    Parameters
    ----------
    name : str
        The job name.
    input_set_generator : .VaspInputGenerator
        A generator used to make the input set.
    write_input_set_kwargs : dict
        Keyword arguments that will get passed to :obj:`.write_vasp_input_set`.
    copy_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.copy_vasp_outputs`.
    run_vasp_kwargs : dict
        Keyword arguments that will get passed to :obj:`.run_vasp`.
    task_document_kwargs : dict
        Keyword arguments that will get passed to :obj:`.TaskDoc.from_directory`.
    stop_children_kwargs : dict
        Keyword arguments that will get passed to :obj:`.should_stop_children`.
    write_additional_data : dict
        Additional data to write to the current directory. Given as a dict of
        {filename: data}. Note that if using FireWorks, dictionary keys cannot contain
        the "." character which is typically used to denote file extensions. To avoid
        this, use the ":" character, which will automatically be converted to ".". E.g.
        ``{"my_file:txt": "contents of the file"}``.
    """

    name: str = "MP meta-GGA static"
    input_set_generator: VaspInputGenerator = field(
        default_factory=lambda: MPMetaGGARelaxGenerator(
            user_incar_settings={
                "NSW": 0,  # zero ionic steps
                "ISMEAR": -5,  # orbital occupancies use tetrahedron method with Blöchl
                "ALGO": "FAST",
                "LREAL": False,  # no real space projection
                "LCHARG": True,  # write CHGCAR
                "LWAVE": False,  # do not write WAVECAR
            },
            auto_ismear=False,  # don't auto-set ISMEAR and SIGMA based on bandgap
        )
    )
