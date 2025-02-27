import random
import math

def slab_transmission(Sig_s, Sig_a, thickness, N):

    Sig_t = Sig_a + Sig_s
    iSig_t = 1 / Sig_t  # Barakat : mean free path
    transmission = 0.0
    N = int(N)
    tot_colls = 0 # ( Modified )

    for i in range(N):
        # For a beam, the initial direction is fixed (mu = 1)
        mu = 1.0 # cos of the angle of the neutron
        x = 0.0
        alive = True
        colls = 0 # For the number of collision for the neutron (Modyfied)

        while alive:
            # Sample distance to the next collision
            l = -math.log(1 - random.random()) * iSig_t
            x += l * mu  # Move particle along the x-direction
            # x = x + (l * mu)

            # Check if the neutron has left the slab
            if x > thickness:
                transmission += 1
                alive = False
            elif x < 0:
                alive = False
            else:
                # Determine if the neutron scatters or gets absorbed
                if random.random() < Sig_s * iSig_t:
                    # Scattering event: choose a new direction (still isotropic scattering)
                    mu = random.uniform(-1, 1)
                    # Count the num of collision for scattering ( Modyfied )
                    colls += 1
                else:
                    # Absorption event: terminate the neutron's history
                    colls += 1 # Count the num of collision for absorbtion (Modyfied)
                    alive = False

        # Add the number of collisions for this neutron to the total
        tot_colls += colls

    # Calculate the average number of collisions # Modified
    avg_colls = tot_colls / N
    return transmission / N , avg_colls # Modified

# Example usage:
N = 100000
Sigma_s = 0.75
Sigma_a = 2.0 - Sigma_s
thickness = 3.0
transmission, avg_colls = slab_transmission(Sigma_s, Sigma_a, thickness, N) # Modified

print("Out of", N, "neutrons, only", int ( transmission * N ),
"made it through.\nThe fraction that made it through was", transmission)
print ("Average collisions per neutron:", avg_colls) # Modified