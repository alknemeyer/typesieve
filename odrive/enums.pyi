# add code to generate this?

GPIO_MODE_DIGITAL: int
GPIO_MODE_DIGITAL_PULL_UP: int
GPIO_MODE_DIGITAL_PULL_DOWN: int
GPIO_MODE_ANALOG_IN: int
GPIO_MODE_UART0: int
GPIO_MODE_UART1: int
GPIO_MODE_UART2: int
GPIO_MODE_CAN0: int
GPIO_MODE_I2C0: int
GPIO_MODE_SPI0: int
GPIO_MODE_PWM0: int
GPIO_MODE_ENC0: int
GPIO_MODE_ENC1: int
GPIO_MODE_ENC2: int
GPIO_MODE_MECH_BRAKE: int

# ODrive.Can.Protocol
PROTOCOL_SIMPLE: int

# ODrive.Axis.AxisState
AXIS_STATE_UNDEFINED: int
AXIS_STATE_IDLE: int
AXIS_STATE_STARTUP_SEQUENCE: int
AXIS_STATE_FULL_CALIBRATION_SEQUENCE: int
AXIS_STATE_MOTOR_CALIBRATION: int
AXIS_STATE_SENSORLESS_CONTROL: int
AXIS_STATE_ENCODER_INDEX_SEARCH: int
AXIS_STATE_ENCODER_OFFSET_CALIBRATION: int
AXIS_STATE_CLOSED_LOOP_CONTROL: int
AXIS_STATE_LOCKIN_SPIN: int
AXIS_STATE_ENCODER_DIR_FIND: int
AXIS_STATE_HOMING: int

# ODrive.ThermistorCurrentLimiter.Error
THERMISTOR_CURRENT_LIMITER_ERROR_NONE: int
THERMISTOR_CURRENT_LIMITER_ERROR_OVER_TEMP: int

# ODrive.Encoder.Mode
ENCODER_MODE_INCREMENTAL: int
ENCODER_MODE_HALL: int
ENCODER_MODE_SINCOS: int
ENCODER_MODE_SPI_ABS_CUI: int
ENCODER_MODE_SPI_ABS_AMS: int
ENCODER_MODE_SPI_ABS_AEAT: int
ENCODER_MODE_SPI_ABS_RLS: int

# ODrive.Controller.ControlMode
# current lib is CONTROL_MODE_POSITION_CONTROL?
CTRL_MODE_VOLTAGE_CONTROL: int
CTRL_MODE_TORQUE_CONTROL: int
CTRL_MODE_VELOCITY_CONTROL: int
CTRL_MODE_POSITION_CONTROL: int

# ODrive.Controller.InputMode
INPUT_MODE_INACTIVE: int
INPUT_MODE_PASSTHROUGH: int
INPUT_MODE_VEL_RAMP: int
INPUT_MODE_POS_FILTER: int
INPUT_MODE_MIX_CHANNELS: int
INPUT_MODE_TRAP_TRAJ: int
INPUT_MODE_TORQUE_RAMP: int
INPUT_MODE_MIRROR: int

# ODrive.Motor.MotorType
MOTOR_TYPE_HIGH_CURRENT: int
MOTOR_TYPE_GIMBAL: int
MOTOR_TYPE_ACIM: int

# ODrive.Can.Error
CAN_ERROR_NONE: int
CAN_ERROR_DUPLICATE_CAN_IDS: int

# ODrive.Axis.Error
AXIS_ERROR_NONE: int
AXIS_ERROR_INVALID_STATE: int
AXIS_ERROR_DC_BUS_UNDER_VOLTAGE: int
AXIS_ERROR_DC_BUS_OVER_VOLTAGE: int
AXIS_ERROR_CURRENT_MEASUREMENT_TIMEOUT: int
AXIS_ERROR_BRAKE_RESISTOR_DISARMED: int
AXIS_ERROR_MOTOR_DISARMED: int
AXIS_ERROR_MOTOR_FAILED: int
AXIS_ERROR_SENSORLESS_ESTIMATOR_FAILED: int
AXIS_ERROR_ENCODER_FAILED: int
AXIS_ERROR_CONTROLLER_FAILED: int
AXIS_ERROR_POS_CTRL_DURING_SENSORLESS: int
AXIS_ERROR_WATCHDOG_TIMER_EXPIRED: int
AXIS_ERROR_MIN_ENDSTOP_PRESSED: int
AXIS_ERROR_MAX_ENDSTOP_PRESSED: int
AXIS_ERROR_ESTOP_REQUESTED: int
AXIS_ERROR_HOMING_WITHOUT_ENDSTOP: int
AXIS_ERROR_OVER_TEMP: int

# ODrive.Axis.LockinState
LOCKIN_STATE_INACTIVE: int
LOCKIN_STATE_RAMP: int
LOCKIN_STATE_ACCELERATE: int
LOCKIN_STATE_CONST_VEL: int

# ODrive.Motor.Error
MOTOR_ERROR_NONE: int
MOTOR_ERROR_PHASE_RESISTANCE_OUT_OF_RANGE: int
MOTOR_ERROR_PHASE_INDUCTANCE_OUT_OF_RANGE: int
MOTOR_ERROR_ADC_FAILED: int
MOTOR_ERROR_DRV_FAULT: int
MOTOR_ERROR_CONTROL_DEADLINE_MISSED: int
MOTOR_ERROR_NOT_IMPLEMENTED_MOTOR_TYPE: int
MOTOR_ERROR_BRAKE_CURRENT_OUT_OF_RANGE: int
MOTOR_ERROR_MODULATION_MAGNITUDE: int
MOTOR_ERROR_BRAKE_DEADTIME_VIOLATION: int
MOTOR_ERROR_UNEXPECTED_TIMER_CALLBACK: int
MOTOR_ERROR_CURRENT_SENSE_SATURATION: int
MOTOR_ERROR_CURRENT_LIMIT_VIOLATION: int
MOTOR_ERROR_BRAKE_DUTY_CYCLE_NAN: int
MOTOR_ERROR_DC_BUS_OVER_REGEN_CURRENT: int
MOTOR_ERROR_DC_BUS_OVER_CURRENT: int
MOTOR_ERROR_MODULATION_IS_NAN: int

# ODrive.Motor.ArmedState
ARMED_STATE_DISARMED: int
ARMED_STATE_WAITING_FOR_TIMINGS: int
ARMED_STATE_WAITING_FOR_UPDATE: int
ARMED_STATE_ARMED: int

# ODrive.Controller.Error
CONTROLLER_ERROR_NONE: int
CONTROLLER_ERROR_OVERSPEED: int
CONTROLLER_ERROR_INVALID_INPUT_MODE: int
CONTROLLER_ERROR_UNSTABLE_GAIN: int
CONTROLLER_ERROR_INVALID_MIRROR_AXIS: int
CONTROLLER_ERROR_INVALID_LOAD_ENCODER: int
CONTROLLER_ERROR_INVALID_ESTIMATE: int

# ODrive.Encoder.Error
ENCODER_ERROR_NONE: int
ENCODER_ERROR_UNSTABLE_GAIN: int
ENCODER_ERROR_CPR_POLEPAIRS_MISMATCH: int
ENCODER_ERROR_NO_RESPONSE: int
ENCODER_ERROR_UNSUPPORTED_ENCODER_MODE: int
ENCODER_ERROR_ILLEGAL_HALL_STATE: int
ENCODER_ERROR_INDEX_NOT_FOUND_YET: int
ENCODER_ERROR_ABS_SPI_TIMEOUT: int
ENCODER_ERROR_ABS_SPI_COM_FAIL: int
ENCODER_ERROR_ABS_SPI_NOT_READY: int

# ODrive.SensorlessEstimator.Error
SENSORLESS_ESTIMATOR_ERROR_NONE: int
SENSORLESS_ESTIMATOR_ERROR_UNSTABLE_GAIN: int