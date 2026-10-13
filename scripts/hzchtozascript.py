from engine_runtime import Behaviour

# region MYENGINE_BLUEPRINT
def _bp_start(self, dt=0.0):
    pass

def _bp_update(self, dt=0.0):
    # Rotate node '4'
    self.entity.rotate(0, (30 * dt), 0)
    # Branch node '10'
    if self.world.input.down('Y'):
        # Spawn node '7'
        self.world.instantiate('assets/Cube.obj', position=(0, 2, 0), scripts=[])
    else:
        pass

def _bp_fixed_update(self, dt=0.0):
    pass

# endregion MYENGINE_BLUEPRINT

class Script(Behaviour):
    def start(self):
        _bp_start(self)

    def update(self, dt):
        _bp_update(self, dt)

    def fixed_update(self, dt):
        _bp_fixed_update(self, dt)

# Write your extra Python outside the generated region.
