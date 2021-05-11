/** Information about a Star */
export interface StarData {
  /** Name of the Star */
  name: string;
  /** Distance from the Earth (in Light Years) */
  distance: number;
  /** Mass of the Star (in Solar Mass) */
  mass: number;
  /** Radius of the Star (in Solar Radius) */
  radius: number;
  /** Acceleration due to Gravity of the Star (in meters per second squared) */
  gravity: number;
}
