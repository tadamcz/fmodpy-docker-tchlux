import fmodpy

from mypackage import PROJECT_ROOT

if __name__ == "__main__":
    mqsi_dir = f"{PROJECT_ROOT}/tchlux/mqsi"

    fmodpy.fimport(
        f"{mqsi_dir}/MQSI.f90",
        dependencies=[
            f"{mqsi_dir}/REAL_PRECISION.f90",
            f"{mqsi_dir}/EVAL_BSPLINE.f90",
            f"{mqsi_dir}/SPLINE.f90",
        ],
        blas=True,
        lapack=True,
        output_dir=f"{PROJECT_ROOT}/mypackage",
        verbose=True,
    )

    fmodpy.fimport(
        f"{mqsi_dir}/SPLINE.f90",
        dependencies=[
            f"{mqsi_dir}/REAL_PRECISION.f90",
            f"{mqsi_dir}/EVAL_BSPLINE.f90",
        ],
        blas=True,
        lapack=True,
        output_dir=f"{PROJECT_ROOT}/mypackage",
        verbose=True,
    )
