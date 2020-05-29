"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Setup package for this sensor (based on this project) made by
# m1ch3al (renato.sirola@gmail.com)

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name="adafruit-circuitpython-mpu6050",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="CircuitPython library for the Gyro/Accel MPU6050-sensor.",
    # The project's main homepage.
    #url="https://github.com/adafruit/Adafruit_CircuitPython_BME280",
    # Author details
    author="m1ch3al",
    author_email="renato.sirola@gmail.com",
    install_requires=["smbus2"],
    # Choose your license
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    # What does your project relate to?
    keywords="adafruit mpu6050 sensor hardware micropython circuitpython",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    py_modules=["adafruit_mpu6050"],
)
