# This is faar from complete.
# The ACTUAL solution would be to either:
#
# copy over the public attributes by hand from:
#   https://github.com/madcowswe/ODrive/tree/devel/Firmware/MotorControl
#   or:
#   https://github.com/madcowswe/ODrive/blob/devel/Firmware/odrive-interface.yaml
#   which goes against all the "automate everything!!" bones in my body,
#   but realistically would be quicker to do and probably not much work
#   to maintain afterwards
#
# or,
#
# use that directory + possibly the fibre thingy to autogenerate .pyi
#   files, which (again) realistically would take more of your time
#   (at least initially) but would be so satisfying once done :)

__all__ = ['find_any']


def find_any() -> ODrive: ...

###


class ODrive:
    axis0: Axis
    axis1: Axis
    vbus_voltage: float
    serial_number: int
    hw_version_major: int
    hw_version_minor: int
    hw_version_variant: int
    fw_version_major: int
    fw_version_minor: int
    fw_version_revision: int
    fw_version_unreleased: int
    user_config_loaded: bool
    brake_resistor_armed: bool
    system_stats: SystemStats
    config: ODriveConfig
    can: CAN
    test_property: int
    def test_function(self, delta: int): ...
    def get_oscilloscope_val(self, index: int): ...
    def get_adc_voltage(self, gpio: int): ...
    def save_configuration(self): ...
    def erase_configuration(self): ...
    def reboot(self): ...
    def enter_dfu_mode(self): ...


class ODriveConfig:
    brake_resistance: float
    enable_uart: bool
    enable_i2c_instead_of_can: bool
    enable_ascii_protocol_on_usb: bool
    dc_bus_undervoltage_trip_level: float
    dc_bus_overvoltage_trip_level: float
    gpio1_pwm_mapping: ...
    gpio2_pwm_mapping: ...
    gpio3_pwm_mapping: ...
    gpio4_pwm_mapping: ...
    gpio3_analog_mapping: ...
    gpio4_analog_mapping: ...


class CAN:
    error: int
    config: ...
    can_protocol: int
    def set_baud_rate(self, baudRate: int): ...


class SystemStats:
    uptime: int
    min_heap_space: int
    min_stack_space_axis0: int
    min_stack_space_axis1: int
    min_stack_space_comms: int
    min_stack_space_usb: int
    min_stack_space_uart: int
    min_stack_space_can: int
    min_stack_space_usb_irq: int
    min_stack_space_startup: int
    usb: ...
    i2c: ...

###


class Axis:
    error: int
    step_dir_active: bool
    current_state: int
    requested_state: int
    loop_counter: int
    lockin_state: int
    controller: Controller
    encoder: Encoder
    sensorless_estimator: SensorlessEstimator
    motor: Motor
    trap_traj: TrapTraj
    config: AxisConfig
    # watchdog_feed


class AxisConfig:
    startup_motor_calibration: bool
    startup_encoder_index_search: bool
    startup_encoder_offset_calibration: bool
    startup_closed_loop_control: bool
    startup_sensorless_control: bool
    enable_step_dir: bool
    counts_per_step: float
    watchdog_timeout: float
    step_gpio_pin: int
    dir_gpio_pin: int
    can_node_id: int
    can_heartbeat_rate_ms: int
    calibration_lockin: ...
    sensorless_ramp: ...
    general_lockin: ...


class SensorlessEstimator:
    error: int
    phase: float
    pll_pos: float
    vel_estimate: float
    config: ...


# possibly incomplete!
class TrapTraj:
    config: TrapTrapConfig

# possible incomplete!
class TrapTrapConfig:
    vel_limit: float  # the maximum planned trajectory speed. This sets your coasting speed
    accel_limit: float # the maximum acceleration in counts / sec^2
    decel_limit: float # the maximum deceleration in counts / sec^2
    # a value which correlates acceleration (in counts / sec^2) and motor current.
    # It is 0 by default. It is optional, but can improve response of your system
    # if correctly tuned. Keep in mind this will need to change with the load / mass of your system.
    A_per_css: float

###


class Motor:
    error: int
    armed_state: int
    is_calibrated: bool
    current_meas_phB: float
    current_meas_phC: float
    DC_calib_phB: float
    DC_calib_phC: float
    phase_current_rev_gain: float
    thermal_current_lim: float
    get_inverter_temp: ...
    current_control: ...
    gate_driver: ...
    timing_log: ...
    config: ...

###


class Controller:
    error: int
    pos_setpoint: float
    vel_setpoint: float
    vel_integrator_current: float
    current_setpoint: float
    vel_ramp_target: float
    config: ControllerConfig

    def set_pos_setpoint(self, pos_setpoint: float,
                         vel_feed_forward: float, current_feed_forward: float): ...
    def set_vel_setpoint(self, vel_setpoint: float,
                         current_feed_forward: float): ...

    def set_current_setpoint(self, current_setpoint: float): ...
    def move_to_pos(self, pos_setpoint: float): ...
    def move_incremental(self, displacement: float, from_goal_point: bool): ...
    def start_anticogging_calibration(self): ...


class ControllerConfig:
    control_mode: int
    pos_gain: float
    vel_gain: float
    vel_integrator_gain: float
    vel_limit: float
    vel_limit_tolerance: float
    vel_ramp_enable: bool
    vel_ramp_rate: float
    setpoints_in_cpr: bool

###


class Encoder:
    error: int
    is_ready: bool
    index_found: bool
    shadow_count: int
    count_in_cpr: int
    interpolation: float
    phase: float
    pos_estimate: float
    pos_cpr: float
    hall_state: int
    vel_estimate: float
    calib_scan_response: float
    config: EncoderConfig
    def set_linear_count(self, count: int): ...


class EncoderConfig:
    mode: int
    use_index: bool
    find_idx_on_lockin_only: bool
    zero_count_on_find_idx: bool
    cpr: int
    offset: int
    pre_calibrated: bool
    offset_float: float
    enable_phase_interpolation: bool
    bandwidth: float
    calib_range: float
    calib_scan_distance: float
    calib_scan_omega: float
    idx_search_unidirectional: bool
    ignore_illegal_hall_state: bool
