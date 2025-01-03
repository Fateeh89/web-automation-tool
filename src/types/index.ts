export interface JumpboxConnection {
    id: string;
    hostname: string;
    username: string;
    password: string;
    port: number;
}

export interface Device {
    id: string;
    type: string;
    ipAddress: string;
    status: string;
}

export interface ReportData {
    title: string;
    date: Date;
    performanceMetrics: {
        cpuUsage: number;
        memoryUsage: number;
        networkTraffic: number;
    };
}